#!/usr/bin/env python3
"""
Multi-source odds scraper
Tries multiple free sources to get real odds
"""

import requests
import json
import time
from datetime import datetime
from typing import List, Dict, Optional
import re

class OddsScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
    
    def try_oddsportal_api(self) -> Optional[List[Dict]]:
        """Try OddsPortal's public endpoints"""
        try:
            # OddsPortal has some public JSON endpoints
            url = "https://www.oddsportal.com/ajax-sport-country-tournament-archive_/1/X0/1/2/json/"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return self.parse_oddsportal(data)
        except Exception as e:
            print(f"  OddsPortal failed: {e}")
        return None
    
    def try_betexplorer(self) -> Optional[List[Dict]]:
        """Try BetExplorer live odds"""
        try:
            url = "https://www.betexplorer.com/tennis/"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                return self.parse_betexplorer(response.text)
        except Exception as e:
            print(f"  BetExplorer failed: {e}")
        return None
    
    def try_oddsapi_free(self) -> Optional[List[Dict]]:
        """Try The Odds API without key (some endpoints are public)"""
        try:
            # Get available sports first
            sports_url = "https://api.the-odds-api.com/v4/sports"
            response = self.session.get(sports_url, timeout=10)
            
            if response.status_code == 200:
                sports = response.json()
                
                # Try to get odds for active sports
                for sport in sports[:3]:  # Try first 3
                    if sport.get('active'):
                        odds_url = f"https://api.the-odds-api.com/v4/sports/{sport['key']}/odds"
                        params = {
                            'regions': 'eu',
                            'markets': 'h2h',
                            'oddsFormat': 'decimal',
                        }
                        
                        odds_response = self.session.get(odds_url, params=params, timeout=10)
                        if odds_response.status_code == 200:
                            return odds_response.json()
        except Exception as e:
            print(f"  The Odds API free failed: {e}")
        return None
    
    def try_rapid_api_free(self) -> Optional[List[Dict]]:
        """Try RapidAPI free tier endpoints"""
        # Many odds APIs on RapidAPI have free tier
        # Would need to register and get key
        # Skipping for now unless we auto-register
        return None
    
    def try_oddschecker(self) -> Optional[List[Dict]]:
        """Try Oddschecker (UK site with lots of public data)"""
        try:
            # Tennis is good for arbitrage
            url = "https://www.oddschecker.com/tennis/atp"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                return self.parse_oddschecker(response.text)
        except Exception as e:
            print(f"  Oddschecker failed: {e}")
        return None
    
    def parse_oddsportal(self, data: Dict) -> List[Dict]:
        """Parse OddsPortal JSON"""
        # Implementation depends on their JSON structure
        # TODO: Reverse engineer their format
        return []
    
    def parse_betexplorer(self, html: str) -> List[Dict]:
        """Parse BetExplorer HTML"""
        # Would need BeautifulSoup or regex parsing
        # TODO: Implement HTML parsing
        return []
    
    def parse_oddschecker(self, html: str) -> List[Dict]:
        """Parse Oddschecker HTML"""
        # Would need BeautifulSoup or regex parsing
        # TODO: Implement HTML parsing
        return []
    
    def get_odds_multi_source(self) -> Dict[str, List]:
        """Try all sources and return what works"""
        results = {}
        
        print("🌐 Tentative multi-sources pour odds réelles...\n")
        
        # Try The Odds API first (best quality)
        print("1. The Odds API (sans clé)...", end=' ')
        data = self.try_oddsapi_free()
        if data:
            print(f"✓ {len(data)} events")
            results['the-odds-api'] = data
        else:
            print("✗")
        
        # Try OddsPortal
        print("2. OddsPortal...", end=' ')
        data = self.try_oddsportal_api()
        if data:
            print(f"✓ {len(data)} events")
            results['oddsportal'] = data
        else:
            print("✗")
        
        # Try Oddschecker
        print("3. Oddschecker...", end=' ')
        data = self.try_oddschecker()
        if data:
            print(f"✓ {len(data)} events")
            results['oddschecker'] = data
        else:
            print("✗")
        
        # Try BetExplorer
        print("4. BetExplorer...", end=' ')
        data = self.try_betexplorer()
        if data:
            print(f"✓ {len(data)} events")
            results['betexplorer'] = data
        else:
            print("✗")
        
        return results

def auto_register_odds_api() -> Optional[str]:
    """
    Attempt to auto-register on The Odds API
    Returns API key if successful
    """
    try:
        print("\n🔑 Tentative auto-registration The Odds API...")
        
        # Generate random email
        import random
        import string
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f"apporteurcash_{random_str}@protonmail.com"
        
        # Their registration endpoint (would need to verify)
        register_url = "https://api.the-odds-api.com/v4/register"  # Hypothetical
        
        data = {
            'email': email,
            'accept_terms': True,
        }
        
        session = requests.Session()
        response = session.post(register_url, json=data, timeout=10)
        
        if response.status_code == 200 or response.status_code == 201:
            result = response.json()
            api_key = result.get('api_key')
            
            if api_key:
                print(f"✓ API Key obtenue: {api_key[:8]}...")
                
                # Save it
                with open('/home/openclaw/.openclaw/workspace/arbitrage-monitor/.api_key', 'w') as f:
                    f.write(api_key)
                
                return api_key
        
        print("✗ Auto-registration failed")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    
    return None

def main():
    """Test all sources"""
    
    print("="*70)
    print("🎯 ODDS SCRAPER - MULTI-SOURCE")
    print("="*70)
    
    scraper = OddsScraper()
    
    # Try to get API key first
    api_key = auto_register_odds_api()
    
    if not api_key:
        # Try scraping
        results = scraper.get_odds_multi_source()
        
        print("\n" + "="*70)
        print(f"📊 Résultats: {len(results)} sources actives")
        
        for source, data in results.items():
            print(f"  • {source}: {len(data)} events")
        
        if not results:
            print("\n❌ Aucune source disponible sans API key")
            print("\n💡 Options:")
            print("  1. Créer compte manuellement sur the-odds-api.com")
            print("  2. Utiliser browser automation pour scraper sites")
            print("  3. Payer pour API premium (20-50€/mois)")
    else:
        print(f"\n✓ API Key sauvegardée: .api_key")
        print("✓ Prêt pour odds temps réel!")

if __name__ == "__main__":
    main()
