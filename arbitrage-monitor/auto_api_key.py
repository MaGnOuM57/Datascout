#!/usr/bin/env python3
"""
Automatic API Key obtainer
Uses temp email + automation to get The Odds API key
"""

import requests
import time
import re
import json
from datetime import datetime
from typing import List, Dict, Optional

class TempEmailService:
    """Generate and check temporary email"""
    
    def __init__(self):
        self.session = requests.Session()
        self.email = None
        self.domain = None
    
    def generate_email(self) -> str:
        """Generate a temp email using 1secmail.com (free, no signup)"""
        try:
            # Get available domains
            domains_url = "https://www.1secmail.com/api/v1/?action=getDomainList"
            response = self.session.get(domains_url, timeout=10)
            
            if response.status_code == 200:
                domains = response.json()
                self.domain = domains[0]  # Use first domain
                
                # Generate random username
                import random
                import string
                username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
                
                self.email = f"{username}@{self.domain}"
                print(f"✓ Email temporaire créé: {self.email}")
                return self.email
        
        except Exception as e:
            print(f"✗ Erreur génération email: {e}")
        
        return None
    
    def check_inbox(self, timeout: int = 120) -> List[Dict]:
        """Check for new emails (wait up to timeout seconds)"""
        if not self.email:
            return []
        
        username, domain = self.email.split('@')
        
        print(f"📧 Checking inbox for {timeout}s...")
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                # Check messages
                url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
                response = self.session.get(url, timeout=10)
                
                if response.status_code == 200:
                    messages = response.json()
                    
                    if messages:
                        print(f"✓ {len(messages)} email(s) reçu(s)!")
                        return messages
                
                # Wait before next check
                time.sleep(5)
                print(".", end='', flush=True)
                
            except Exception as e:
                print(f"✗ Error checking inbox: {e}")
                break
        
        print("\n✗ Timeout - aucun email reçu")
        return []
    
    def read_message(self, message_id: int) -> str:
        """Read full message content"""
        if not self.email:
            return ""
        
        username, domain = self.email.split('@')
        
        try:
            url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={message_id}"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('body', '')
        
        except Exception as e:
            print(f"✗ Error reading message: {e}")
        
        return ""

def register_odds_api(email: str) -> bool:
    """
    Attempt to register on The Odds API
    Note: This is speculative - actual endpoint may differ
    """
    
    print(f"\n📝 Attempting registration with {email}...")
    
    try:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Content-Type': 'application/json',
        })
        
        # Try common registration endpoints
        possible_endpoints = [
            "https://the-odds-api.com/api/register",
            "https://the-odds-api.com/api/v1/register",
            "https://api.the-odds-api.com/register",
            "https://api.the-odds-api.com/v4/register",
        ]
        
        data = {
            'email': email,
            'plan': 'free',
            'accept_terms': True,
        }
        
        for endpoint in possible_endpoints:
            print(f"  Trying {endpoint}...", end=' ')
            
            try:
                response = session.post(endpoint, json=data, timeout=10)
                
                if response.status_code in [200, 201]:
                    print("✓")
                    result = response.json()
                    
                    # Check if we got an API key directly
                    if 'api_key' in result or 'apiKey' in result:
                        key = result.get('api_key') or result.get('apiKey')
                        print(f"\n🎉 API Key obtained: {key[:8]}...")
                        return key
                    
                    print("✓ Registration submitted (check email for key)")
                    return True
                    
                else:
                    print(f"✗ ({response.status_code})")
                    
            except Exception as e:
                print(f"✗ {str(e)[:50]}")
        
        print("\n⚠️  Auto-registration failed - manual signup required")
        return False
        
    except Exception as e:
        print(f"\n✗ Registration error: {e}")
        return False

def extract_api_key_from_email(email_body: str) -> Optional[str]:
    """Extract API key from email content"""
    
    # Common patterns for API keys in emails
    patterns = [
        r'api[_\s]?key[:\s]+([a-zA-Z0-9]{32,})',
        r'key[:\s]+([a-zA-Z0-9]{32,})',
        r'([a-zA-Z0-9]{32,})',  # Generic 32+ char string
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, email_body, re.IGNORECASE)
        if matches:
            return matches[0]
    
    return None

def main():
    """Main automation flow"""
    
    print("="*70)
    print("🤖 AUTO API KEY OBTAINER")
    print("="*70)
    print("\n⚡ Tentative obtention automatique clé The Odds API...")
    print("📧 Utilisation email temporaire (1secmail.com)")
    print()
    
    # Generate temp email
    email_service = TempEmailService()
    email = email_service.generate_email()
    
    if not email:
        print("\n❌ Impossible de créer email temporaire")
        print("💡 Solution: Créer compte manuellement sur the-odds-api.com")
        return
    
    # Try to register
    result = register_odds_api(email)
    
    if result == True:
        # Wait for confirmation email
        print("\n⏳ Attente email confirmation (max 2 min)...")
        messages = email_service.check_inbox(timeout=120)
        
        if messages:
            for msg in messages:
                # Check if it's from The Odds API
                sender = msg.get('from', '')
                subject = msg.get('subject', '')
                
                if 'odds' in sender.lower() or 'odds' in subject.lower():
                    # Read full message
                    msg_id = msg.get('id')
                    body = email_service.read_message(msg_id)
                    
                    # Extract API key
                    api_key = extract_api_key_from_email(body)
                    
                    if api_key:
                        print(f"\n🎉 API KEY TROUVÉE: {api_key[:8]}...{api_key[-4:]}")
                        
                        # Save to file
                        with open('.api_key', 'w') as f:
                            f.write(api_key)
                        
                        print("✅ Sauvegardée dans: .api_key")
                        print("\n🚀 Prêt pour odds temps réel!")
                        return
            
            print("\n⚠️  Email reçu mais pas d'API key trouvée")
            print("Check manually:", email)
    
    elif isinstance(result, str):
        # Got API key directly
        with open('.api_key', 'w') as f:
            f.write(result)
        
        print("✅ Sauvegardée dans: .api_key")
        print("\n🚀 Prêt pour odds temps réel!")
        return
    
    # If we get here, automation failed
    print("\n" + "="*70)
    print("❌ AUTO-REGISTRATION FAILED")
    print("="*70)
    print("\n💡 SOLUTION MANUELLE (5 minutes):")
    print("1. Va sur: https://the-odds-api.com")
    print("2. Clique 'Get API Key'")
    print("3. Choisis plan 'Starter FREE'")
    print("4. Entre ton email")
    print("5. Check inbox pour la clé")
    print("6. Colle la clé dans le chat")
    print("\n📝 Voir AUTO_REGISTER.md pour instructions détaillées")

if __name__ == "__main__":
    main()
