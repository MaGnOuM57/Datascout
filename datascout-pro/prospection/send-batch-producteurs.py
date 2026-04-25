#!/usr/bin/env python3
"""
Envoi sécurisé batch producteurs bio
- Warmup progressif (1 email/heure)
- Vérification bounce après chaque envoi
- Auto-stop si bounce >10%
"""
import requests
import json
import time
from datetime import datetime

API_KEY = "re_bRV78NGE_JtTkPnxngK9DK37tkojWvPRh"
FROM_EMAIL = "contact@ellievai.com"
FROM_NAME = "Ellie VAI"

# Load batch
with open('batch-1-producteurs-ready.json', 'r', encoding='utf-8') as f:
    batch = json.load(f)

def send_email(to, subject, body):
    """Send via Resend API"""
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "from": f"{FROM_NAME} <{FROM_EMAIL}>",
        "to": [to],
        "subject": subject,
        "text": body
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.status_code, response.json()

def check_email_status(email_id):
    """Check delivery status via Resend API"""
    url = f"https://api.resend.com/emails/{email_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('last_event', 'unknown')
    return 'unknown'

def calculate_bounce_rate(results):
    """Calculate bounce rate from results"""
    if not results:
        return 0
    
    bounced = sum(1 for r in results if r.get('status') == 'bounced')
    return (bounced / len(results)) * 100

# Send emails with warmup
print("🚀 Batch 1 Producteurs - Warmup mode")
print(f"📧 Total: {len(batch['emails'])} emails")
print(f"⏱️ Spacing: 1 hour between each")
print("")

results = []
DELAY_SECONDS = 3600  # 1 hour = 3600 seconds

for i, email in enumerate(batch['emails'], 1):
    print(f"\n[{i}/{len(batch['emails'])}] Sending to {email['prospect']['nom']}...")
    print(f"   Email: {email['to']}")
    print(f"   Subject: {email['subject']}")
    
    # Send
    status_code, response = send_email(
        email['to'],
        email['subject'],
        email['body']
    )
    
    if status_code == 200:
        email_id = response.get('id')
        print(f"   ✅ Sent (ID: {email_id})")
        
        # Wait 10 min then check status
        print(f"   ⏳ Waiting 10 min to check delivery...")
        time.sleep(600)  # 10 minutes
        
        status = check_email_status(email_id)
        print(f"   📊 Status: {status}")
        
        results.append({
            "email": email['to'],
            "email_id": email_id,
            "status": status,
            "sent_at": datetime.now().isoformat(),
            "prospect": email['prospect']
        })
        
        # Calculate bounce rate
        bounce_rate = calculate_bounce_rate(results)
        print(f"   📈 Bounce rate: {bounce_rate:.1f}%")
        
        # Auto-stop if bounce >10%
        if bounce_rate > 10 and len(results) >= 3:
            print(f"\n🛑 AUTO-STOP: Bounce rate {bounce_rate:.1f}% > 10%")
            print(f"   Sent: {len(results)}/{len(batch['emails'])}")
            break
        
        # Wait 1 hour before next email (minus the 10 min already waited)
        if i < len(batch['emails']):
            remaining = DELAY_SECONDS - 600
            print(f"   ⏱️ Waiting {remaining//60} min before next email...")
            time.sleep(remaining)
    else:
        print(f"   ❌ Failed: {response}")
        results.append({
            "email": email['to'],
            "status": "failed",
            "error": response,
            "sent_at": datetime.now().isoformat(),
            "prospect": email['prospect']
        })

# Save results
output = {
    "batch_id": batch['batch_id'],
    "completed_at": datetime.now().isoformat(),
    "sent": len([r for r in results if r['status'] not in ['failed', 'bounced']]),
    "bounced": len([r for r in results if r['status'] == 'bounced']),
    "failed": len([r for r in results if r['status'] == 'failed']),
    "bounce_rate": calculate_bounce_rate(results),
    "results": results
}

filename = f"results-batch-1-{datetime.now().strftime('%Y%m%d-%H%M')}.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\n\n✅ Batch 1 complete")
print(f"📊 Sent: {output['sent']}")
print(f"📊 Bounced: {output['bounced']}")
print(f"📊 Failed: {output['failed']}")
print(f"📊 Bounce rate: {output['bounce_rate']:.1f}%")
print(f"💾 Results: {filename}")
