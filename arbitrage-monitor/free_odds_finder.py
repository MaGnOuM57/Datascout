#!/usr/bin/env python3
"""
Free odds finder - No API key required
Uses publicly available odds data
"""

import requests
import json
from datetime import datetime
from typing import List, Dict

class FreeOddsFinder:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def try_betfair_exchange(self) -> List[Dict]:
        """
        Betfair Exchange has some public endpoints
        """
        try:
            # Betfair public API (no login required for some data)
            url = "https://www.betfair.com/exchange/plus/en/tennis-betting-1"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                # Would need to parse HTML
                print(f"✓ Betfair accessible ({len(response.text)} bytes)")
                return []
        except Exception as e:
            print(f"✗ Betfair: {e}")
        return []
    
    def try_pinnacle_public(self) -> List[Dict]:
        """
        Pinnacle sometimes has public feeds
        """
        try:
            # Pinnacle odds feed
            url = "https://guest.api.arcadia.pinnacle.com/0.1/leagues/tennis/matchups"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Pinnacle: {len(data)} items")
                return data
        except Exception as e:
            print(f"✗ Pinnacle: {e}")
        return []
    
    def try_flashscore_api(self) -> List[Dict]:
        """
        FlashScore has hidden API endpoints
        """
        try:
            url = "https://d.flashscore.com/x/feed/df_st_1_"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                print(f"✓ FlashScore accessible")
                return []
        except Exception as e:
            print(f"✗ FlashScore: {e}")
        return []
    
    def try_sofascore_api(self) -> List[Dict]:
        """
        SofaScore has API for live sports
        """
        try:
            # Tennis live events
            url = "https://api.sofascore.com/api/v1/sport/tennis/events/live"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                events = data.get('events', [])
                print(f"✓ SofaScore: {len(events)} live events")
                
                # Get odds for each event
                odds_data = []
                for event in events[:5]:  # Limit to first 5
                    event_id = event.get('id')
                    if event_id:
                        odds_url = f"https://api.sofascore.com/api/v1/event/{event_id}/odds/1/all"
                        odds_resp = self.session.get(odds_url, timeout=10)
                        if odds_resp.status_code == 200:
                            odds_data.append(odds_resp.json())
                
                return odds_data
        except Exception as e:
            print(f"✗ SofaScore: {e}")
        return []
    
    def try_livesport_api(self) -> List[Dict]:
        """
        LiveSport (365scores style) public API
        """
        try:
            url = "https://webws.365scores.com/web/games/?appTypeId=5&langId=1&competitions=45"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✓ LiveSport: {len(data.get('games', []))} games")
                return data.get('games', [])
        except Exception as e:
            print(f"✗ LiveSport: {e}")
        return []
    
    def try_betexplorer_json(self) -> List[Dict]:
        """
        BetExplorer has JSON endpoints for odds
        """
        try:
            # Tennis today
            url = "https://www.betexplorer.com/next/tennis/"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                print(f"✓ BetExplorer accessible")
                # Would need JSON parsing
                return []
        except Exception as e:
            print(f"✗ BetExplorer: {e}")
        return []
    
    def scan_all_sources(self) -> Dict[str, List]:
        """Try all free sources"""
        
        print("🌐 Scanning free odds sources...")
        print("="*70)
        
        sources = {
            'sofascore': self.try_sofascore_api,
            'livesport': self.try_livesport_api,
            'pinnacle': self.try_pinnacle_public,
            'betfair': self.try_betfair_exchange,
            'flashscore': self.try_flashscore_api,
            'betexplorer': self.try_betexplorer_json,
        }
        
        results = {}
        
        for name, func in sources.items():
            print(f"\n{name}...", end=' ')
            try:
                data = func()
                if data:
                    results[name] = data
            except Exception as e:
                print(f"Error: {e}")
        
        return results

def main():
    """Test all free sources"""
    
    print("\n" + "="*70)
    print("🆓 FREE ODDS FINDER - No API Key Required")
    print("="*70)
    
    finder = FreeOddsFinder()
    results = finder.scan_all_sources()
    
    print("\n\n" + "="*70)
    print("📊 RÉSULTATS:")
    print("="*70)
    
    if results:
        for source, data in results.items():
            print(f"\n✓ {source}: {len(data)} items")
            
            # Save
            filename = f'odds_{source}.json'
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"  💾 Saved to: {filename}")
        
        print(f"\n🎯 Total: {len(results)} sources actives")
        print("✅ Données odds disponibles sans API key!")
        
    else:
        print("\n❌ Aucune source gratuite accessible")
        print("\n💡 Solutions:")
        print("  1. Créer compte The Odds API (5 min, gratuit)")
        print("  2. Utiliser browser automation pour scraper")
        print("  3. Payer API premium (~30€/mois)")

if __name__ == "__main__":
    main()
