#!/bin/bash
# Check Resend email delivery status
API_KEY="re_bRV78NGE_JtTkPnxngK9DK37tkojWvPRh"

echo "📧 Checking Resend email delivery status..."
echo ""

# Get emails from batch 1 results
jq -r '.sent[].response.id' prospection/results-20260425-203117.json 2>/dev/null | while read email_id; do
  if [ -n "$email_id" ]; then
    echo "Checking email ID: $email_id"
    curl -s "https://api.resend.com/emails/$email_id" \
      -H "Authorization: Bearer $API_KEY" | jq -r '{id, to, subject, last_event, created_at}'
    echo ""
  fi
done
