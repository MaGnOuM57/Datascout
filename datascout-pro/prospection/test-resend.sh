#!/bin/bash

# Test Resend API - Check domain status

RESEND_API_KEY="re_bRV78NGE_JtTkPnxngK9DK37tkojWvPRh"

echo "🧪 TEST RESEND API - ellievai.com"
echo ""

# Test simple email
echo "Envoi email test..."
RESPONSE=$(curl -s -X POST "https://api.resend.com/emails" \
  -H "Authorization: Bearer $RESEND_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "contact@ellievai.com",
    "to": "delivered@resend.dev",
    "subject": "Test Ellie VAI - Verification",
    "text": "Email test pour vérifier domaine ellievai.com configuré correctement.\n\nSi vous recevez ceci, DNS OK + Resend verified."
  }')

echo "Response:"
echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"

echo ""

# Check si erreur domain not verified
if echo "$RESPONSE" | grep -q "not verified\|not found\|invalid"; then
    echo "❌ ERREUR: Domaine ellievai.com pas encore vérifié dans Resend"
    echo ""
    echo "ACTION REQUISE:"
    echo "1. Va sur https://resend.com/domains"
    echo "2. Add domain: ellievai.com"
    echo "3. Vérifie que DNS records sont détectés (déjà configurés OVH)"
    echo "4. Attends status 'Verified' ✅"
    exit 1
elif echo "$RESPONSE" | grep -q "\"id\""; then
    echo "✅ SUCCESS: Email envoyé! Domaine vérifié."
    echo ""
    echo "PRÊT pour envoi batch prospection."
    exit 0
else
    echo "⚠️  Response inattendue. Check manuellement."
    exit 2
fi
