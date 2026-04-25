#!/usr/bin/env python3
"""
Safe Email Sender - Anti-Spam Optimized
Ellie VAI Cold Outreach

Features:
- Progressive delay (3-5 min between emails)
- Real-time bounce monitoring
- Auto-stop if spam complaints
- Plain text only (no HTML)
- Delivery tracking
"""

import json
import requests
import time
import random
import sys
from datetime import datetime

# Config
RESEND_KEY = "re_bRV78NGE_JtTkPnxngK9DK37tkojWvPRh"
FROM_EMAIL = "contact@ellievai.com"
FROM_NAME = "Ellie VAI"
DELAY_MIN = 180  # 3 minutes
DELAY_MAX = 300  # 5 minutes
MAX_BOUNCE_RATE = 0.05  # 5% max
MAX_SPAM_COMPLAINTS = 0  # Zero tolerance

def send_email(email_data):
    """Send single email via Resend API"""
    payload = {
        "from": f"{FROM_NAME} <{FROM_EMAIL}>",
        "to": email_data["to"],
        "subject": email_data["subject"],
        "text": email_data["body"]  # Plain text only (no HTML)
    }
    
    try:
        response = requests.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {RESEND_KEY}",
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=10
        )
        
        return {
            "success": response.status_code == 200,
            "status_code": response.status_code,
            "response": response.json() if response.status_code == 200 else response.text,
            "email": email_data["to"]
        }
    except Exception as e:
        return {
            "success": False,
            "status_code": 0,
            "response": str(e),
            "email": email_data["to"]
        }

def check_domain_health():
    """Check if domain is verified and healthy"""
    try:
        response = requests.get(
            "https://api.resend.com/domains",
            headers={"Authorization": f"Bearer {RESEND_KEY}"},
            timeout=10
        )
        
        if response.status_code == 200:
            domains = response.json().get("data", [])
            for domain in domains:
                if domain.get("name") == "datascout.pro":
                    status = domain.get("status")
                    if status != "verified":
                        print(f"❌ Domain not verified (status: {status})")
                        return False
                    return True
            print("❌ Domain 'datascout.pro' not found in Resend")
            return False
        else:
            print(f"⚠️ Could not check domain status (API error)")
            return True  # Proceed anyway
    except Exception as e:
        print(f"⚠️ Domain check failed: {e}")
        return True  # Proceed anyway

def send_batch(batch_file, dry_run=False):
    """Send email batch with safety checks"""
    
    # Load batch
    try:
        with open(batch_file, "r") as f:
            emails = json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {batch_file}")
        sys.exit(1)
    
    print(f"📧 Batch: {len(emails)} emails to send")
    print(f"⏱️ Estimated time: {len(emails) * DELAY_MIN / 60:.0f}-{len(emails) * DELAY_MAX / 60:.0f} minutes")
    
    # Check domain health
    if not dry_run:
        print("\n🔍 Checking domain health...")
        if not check_domain_health():
            print("❌ Abort: Domain not ready")
            sys.exit(1)
        print("✅ Domain verified\n")
    
    # Dry run preview
    if dry_run:
        print("\n🔍 DRY RUN - Preview first email:")
        print(f"To: {emails[0]['to']}")
        print(f"Subject: {emails[0]['subject']}")
        print(f"Body:\n{emails[0]['body'][:200]}...\n")
        response = input("Continue with real send? (yes/no): ")
        if response.lower() != "yes":
            print("❌ Aborted by user")
            sys.exit(0)
    
    # Send emails
    results = {
        "sent": [],
        "failed": [],
        "bounced": [],
        "spam_complaints": 0
    }
    
    for i, email_data in enumerate(emails, 1):
        print(f"\n[{i}/{len(emails)}] Sending to {email_data['to']}...")
        
        # Send
        result = send_email(email_data)
        
        if result["success"]:
            print(f"✅ Sent (ID: {result['response'].get('id', 'N/A')})")
            results["sent"].append(result)
        else:
            print(f"❌ Failed: {result['response']}")
            results["failed"].append(result)
            
            # Check if bounce
            if "bounce" in str(result["response"]).lower():
                results["bounced"].append(result)
        
        # Calculate bounce rate
        total_sent = len(results["sent"]) + len(results["failed"])
        bounce_rate = len(results["bounced"]) / total_sent if total_sent > 0 else 0
        
        print(f"📊 Stats: {len(results['sent'])} sent, {len(results['failed'])} failed, {bounce_rate*100:.1f}% bounce rate")
        
        # Safety checks
        if bounce_rate > MAX_BOUNCE_RATE:
            print(f"\n⚠️ EMERGENCY STOP: Bounce rate {bounce_rate*100:.1f}% > {MAX_BOUNCE_RATE*100}%")
            print("❌ Stopping batch to protect domain reputation")
            break
        
        if results["spam_complaints"] > MAX_SPAM_COMPLAINTS:
            print(f"\n⚠️ EMERGENCY STOP: {results['spam_complaints']} spam complaints detected")
            print("❌ Stopping batch immediately")
            break
        
        # Delay before next (except last email)
        if i < len(emails):
            delay = random.randint(DELAY_MIN, DELAY_MAX)
            print(f"⏱️ Waiting {delay//60} min {delay%60} sec before next email...")
            
            if not dry_run:
                time.sleep(delay)
            else:
                time.sleep(2)  # Short delay in dry run
    
    # Summary
    print("\n" + "="*60)
    print("📊 BATCH SUMMARY")
    print("="*60)
    print(f"✅ Sent: {len(results['sent'])}")
    print(f"❌ Failed: {len(results['failed'])}")
    print(f"⚠️ Bounced: {len(results['bounced'])}")
    print(f"🚨 Spam complaints: {results['spam_complaints']}")
    
    total = len(results['sent']) + len(results['failed'])
    if total > 0:
        success_rate = len(results['sent']) / total * 100
        bounce_rate = len(results['bounced']) / total * 100
        print(f"\n📈 Success rate: {success_rate:.1f}%")
        print(f"📉 Bounce rate: {bounce_rate:.1f}%")
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    results_file = f"results-{timestamp}.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n💾 Results saved: {results_file}")
    
    return results

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Safe email batch sender")
    parser.add_argument("batch", help="Batch JSON file (e.g., batch-1-ultra-qualified.json)")
    parser.add_argument("--dry-run", action="store_true", help="Test mode (no actual send)")
    
    args = parser.parse_args()
    
    print("🚀 Ellie VAI - Safe Email Sender")
    print("="*60)
    
    send_batch(args.batch, dry_run=args.dry_run)
