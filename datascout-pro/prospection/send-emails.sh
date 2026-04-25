#!/bin/bash

# Script d'envoi emails - DataScout Pro Prospection
# Usage: ./send-emails.sh [resend|gmail|manual]

METHOD=$1
EMAILS_FILE="emails-batch-1-ready.json"
RESEND_KEY="re_bRV78NGE_JtTkPnxngK9DK37tkojWvPRh"

if [ -z "$METHOD" ]; then
  echo "❌ Usage: ./send-emails.sh [resend|gmail|manual]"
  exit 1
fi

case $METHOD in
  resend)
    echo "🚀 Envoi via Resend API..."
    # Requires domain configured in Resend first
    python3 << 'PYSCRIPT'
import json
import requests
import time

RESEND_KEY = "re_bRV78NGE_JtTkPnxngK9DK37tkojWvPRh"
FROM_EMAIL = "contact@datascout.pro"  # Must be verified domain

with open("emails-batch-1-ready.json", "r") as f:
    emails = json.load(f)

sent = 0
errors = []

for email in emails:
    payload = {
        "from": FROM_EMAIL,
        "to": email["to"],
        "subject": email["subject"],
        "text": email["body"]
    }
    
    response = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {RESEND_KEY}"},
        json=payload
    )
    
    if response.status_code == 200:
        sent += 1
        print(f"✅ {sent}/50 - Sent to {email['to']}")
    else:
        errors.append({"to": email["to"], "error": response.text})
        print(f"❌ Failed: {email['to']} - {response.text}")
    
    time.sleep(1)  # Rate limit: 1 email/sec

print(f"\n📊 Résultat: {sent} envoyés, {len(errors)} erreurs")

if errors:
    with open("send-errors.json", "w") as f:
        json.dump(errors, f, indent=2)
    print("⚠️ Erreurs sauvegardées → send-errors.json")
PYSCRIPT
    ;;
    
  gmail)
    echo "🚀 Envoi via Gmail SMTP..."
    echo "⚠️ Nécessite GMAIL_APP_PASSWORD en variable d'environnement"
    python3 << 'PYSCRIPT'
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time

GMAIL_USER = os.getenv("GMAIL_USER", "your-email@gmail.com")
GMAIL_PASS = os.getenv("GMAIL_APP_PASSWORD")

if not GMAIL_PASS:
    print("❌ GMAIL_APP_PASSWORD not set. Export it first:")
    print('export GMAIL_APP_PASSWORD="your-app-password"')
    exit(1)

with open("emails-batch-1-ready.json", "r") as f:
    emails = json.load(f)

sent = 0
errors = []

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(GMAIL_USER, GMAIL_PASS)

for email in emails:
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = email['to']
    msg['Subject'] = email['subject']
    msg.attach(MIMEText(email['body'], 'plain'))
    
    try:
        server.send_message(msg)
        sent += 1
        print(f"✅ {sent}/50 - Sent to {email['to']}")
        time.sleep(2)  # Rate limit: 30 emails/min max
    except Exception as e:
        errors.append({"to": email['to'], "error": str(e)})
        print(f"❌ Failed: {email['to']} - {str(e)}")

server.quit()
print(f"\n📊 Résultat: {sent} envoyés, {len(errors)} erreurs")

if errors:
    with open("send-errors.json", "w") as f:
        json.dump(errors, f, indent=2)
PYSCRIPT
    ;;
    
  manual)
    echo "📝 Génération fichiers TXT pour envoi manuel..."
    python3 << 'PYSCRIPT'
import json

with open("emails-batch-1-ready.json", "r") as f:
    emails = json.load(f)

for i, email in enumerate(emails, 1):
    filename = f"email-{i:02d}-{email['to'].split('@')[0]}.txt"
    with open(filename, "w") as f:
        f.write(f"TO: {email['to']}\n")
        f.write(f"SUBJECT: {email['subject']}\n")
        f.write(f"\n{email['body']}\n")
    
print(f"✅ {len(emails)} emails générés en fichiers TXT")
print("📧 Copie-colle chaque fichier dans Gmail/Outlook pour envoi manuel")
PYSCRIPT
    ;;
    
  *)
    echo "❌ Méthode invalide: $METHOD"
    echo "Options: resend, gmail, manual"
    exit 1
    ;;
esac
