#!/usr/bin/env python3
"""
Live Sports Arbitrage Detector
Scrapes odds from public sources and detects arbitrage opportunities
Sends Telegram notifications when profitable arbs found
"""

import requests
import time
import json
from datetime import datetime
from typing import List, Dict, Optional
import sys

# The Odds API - Free tier (500 requests/month)
ODDS_API_KEY = "demo"  # We'll use demo or try without key first
ODDS_API_BASE = "https://api.the-odds-api.com/v4"

# Telegram config (from environment or hardcoded)
TELEGRAM_CHAT_ID = "1622073877"
TELEGRAM_BOT_TOKEN = None  # Will be set from openclaw

# Sports to monitor
SPORTS = [
    'soccer_epl',           # English Premier League
    'soccer_spain_la_liga', # La Liga
    'soccer_france_ligue_one', # Ligue 1
    'soccer_germany_bundesliga', # Bundesliga
    'soccer_italy_serie_a',  # Serie A
    'basketball_nba',        # NBA
    'tennis_atp',           # Tennis ATP
    'americanfootball_nfl', # NFL
]

# Bookmakers to monitor
BOOKMAKERS = [
    'betclic',
    'unibet',
    'bet365',
    'bwin',
    'winamax',
]

class ArbitrageDetector:
    def __init__(self):
        self.session = requests.Session()
        self.arbs_found = []
        
    def get_odds(self, sport: str) -> Optional[List[Dict]]:
        """Fetch odds for a sport from The Odds API"""
        try:
            # Try free public API first
            url = f"{ODDS_API_BASE}/sports/{sport}/odds"
            params = {
                'regions': 'eu',
                'markets': 'h2h',  # Head to head (win/lose)
                'oddsFormat': 'decimal',
            }
            
            # Try without API key first (some endpoints are public)
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                # Need API key - try with demo
                params['apiKey'] = ODDS_API_KEY
                response = self.session.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    return response.json()
            
            return None
            
        except Exception as e:
            print(f"Error fetching odds for {sport}: {e}")
            return None
    
    def calculate_arbitrage(self, odds: List[float]) -> Dict:
        """
        Calculate if arbitrage exists
        For 2-way market: 1/odds1 + 1/odds2 < 1 = arbitrage
        Returns: {exists: bool, profit_pct: float, stakes: [float, float]}
        """
        if len(odds) < 2:
            return {'exists': False}
        
        # Calculate implied probabilities
        implied_sum = sum(1/odd for odd in odds)
        
        if implied_sum < 1.0:
            # Arbitrage exists!
            profit_pct = (1 - implied_sum) * 100
            
            # Calculate optimal stakes for 500€ total
            total_stake = 500
            stakes = [(total_stake / (odds[i] * implied_sum)) for i in range(len(odds))]
            
            return {
                'exists': True,
                'profit_pct': profit_pct,
                'stakes': stakes,
                'implied_sum': implied_sum,
                'guaranteed_return': total_stake / implied_sum
            }
        
        return {'exists': False}
    
    def format_arb_message(self, event: Dict, arb: Dict, bookmakers: List[str], odds: List[float]) -> str:
        """Format arbitrage opportunity as Telegram message"""
        msg = "🚨 ARBITRAGE DÉTECTÉ!\n\n"
        
        # Event info
        msg += f"⚽ {event['sport_title']}\n"
        msg += f"🏆 {event['home_team']} vs {event['away_team']}\n"
        msg += f"💰 Profit: {arb['profit_pct']:.2f}% garanti\n\n"
        
        msg += "📊 PARIS:\n"
        for i, (bookmaker, odd, stake) in enumerate(zip(bookmakers, odds, arb['stakes'])):
            outcome = event['home_team'] if i == 0 else event['away_team']
            msg += f"{bookmaker}: {outcome} @ {odd:.2f} → Mise {stake:.0f}€\n"
        
        msg += f"\n✅ RÉSULTAT:\n"
        msg += f"Capital: 500€\n"
        msg += f"Retour garanti: {arb['guaranteed_return']:.2f}€\n"
        msg += f"Profit: {arb['guaranteed_return'] - 500:.2f}€\n\n"
        
        # Add timestamp
        msg += f"⏰ {datetime.now().strftime('%H:%M:%S')}\n"
        
        return msg
    
    def send_telegram(self, message: str):
        """Send notification to Telegram"""
        try:
            # Use openclaw's message tool instead
            print(f"\n{'='*60}")
            print(message)
            print('='*60)
            
            # Also save to file for openclaw to pick up
            with open('/home/openclaw/.openclaw/workspace/arbitrage-monitor/alert.txt', 'w') as f:
                f.write(message)
                f.write(f"\n\nTimestamp: {datetime.now().isoformat()}\n")
                
        except Exception as e:
            print(f"Error sending notification: {e}")
    
    def scan_sport(self, sport: str) -> List[Dict]:
        """Scan one sport for arbitrage opportunities"""
        arbs = []
        
        print(f"Scanning {sport}...", end=' ', flush=True)
        odds_data = self.get_odds(sport)
        
        if not odds_data:
            print("❌ No data")
            return arbs
        
        events_checked = 0
        for event in odds_data:
            events_checked += 1
            
            # Get bookmaker odds for this event
            if 'bookmakers' not in event or len(event['bookmakers']) < 2:
                continue
            
            # Extract h2h odds from different bookmakers
            bookmaker_odds = {}
            for bookmaker in event['bookmakers']:
                if bookmaker['key'] in BOOKMAKERS:
                    for market in bookmaker['markets']:
                        if market['key'] == 'h2h':
                            # Get home and away odds
                            odds = [outcome['price'] for outcome in market['outcomes']]
                            bookmaker_odds[bookmaker['title']] = odds
            
            # Check all combinations of 2 bookmakers
            bookmakers_list = list(bookmaker_odds.keys())
            for i in range(len(bookmakers_list)):
                for j in range(i+1, len(bookmakers_list)):
                    bm1, bm2 = bookmakers_list[i], bookmakers_list[j]
                    
                    # Try different outcome combinations
                    odds1 = bookmaker_odds[bm1]
                    odds2 = bookmaker_odds[bm2]
                    
                    # Best odds for each outcome across the 2 bookmakers
                    if len(odds1) >= 2 and len(odds2) >= 2:
                        # Home win from bm1, away win from bm2
                        arb_odds = [odds1[0], odds2[1]]
                        arb = self.calculate_arbitrage(arb_odds)
                        
                        if arb['exists'] and arb['profit_pct'] > 1.5:
                            arb_info = {
                                'event': event,
                                'arb': arb,
                                'bookmakers': [bm1, bm2],
                                'odds': arb_odds,
                                'outcomes': [event['home_team'], event['away_team']]
                            }
                            arbs.append(arb_info)
                            
                        # Away win from bm1, home win from bm2
                        arb_odds = [odds2[0], odds1[1]]
                        arb = self.calculate_arbitrage(arb_odds)
                        
                        if arb['exists'] and arb['profit_pct'] > 1.5:
                            arb_info = {
                                'event': event,
                                'arb': arb,
                                'bookmakers': [bm2, bm1],
                                'odds': arb_odds,
                                'outcomes': [event['home_team'], event['away_team']]
                            }
                            arbs.append(arb_info)
        
        print(f"✓ {events_checked} events, {len(arbs)} arbs")
        return arbs
    
    def run_scan(self):
        """Run one complete scan of all sports"""
        print(f"\n🔍 SCAN {datetime.now().strftime('%H:%M:%S')}")
        print("-" * 60)
        
        all_arbs = []
        for sport in SPORTS:
            arbs = self.scan_sport(sport)
            all_arbs.extend(arbs)
        
        print(f"\n📊 Total: {len(all_arbs)} arbitrage opportunities")
        
        # Send notifications for new arbs
        for arb_info in all_arbs:
            msg = self.format_arb_message(
                arb_info['event'],
                arb_info['arb'],
                arb_info['bookmakers'],
                arb_info['odds']
            )
            self.send_telegram(msg)
            
            # Limit to top 3 arbs per scan
            if all_arbs.index(arb_info) >= 2:
                break
        
        return len(all_arbs)
    
    def monitor_loop(self, interval: int = 60):
        """Continuous monitoring loop"""
        print("🚀 Starting arbitrage monitor...")
        print(f"📊 Monitoring {len(SPORTS)} sports")
        print(f"🔄 Scan interval: {interval} seconds")
        print(f"💰 Target profit: >1.5%")
        print()
        
        scan_count = 0
        total_arbs = 0
        
        try:
            while True:
                scan_count += 1
                arb_count = self.run_scan()
                total_arbs += arb_count
                
                print(f"\n✓ Scan #{scan_count} complete | Total arbs found: {total_arbs}")
                print(f"⏰ Next scan in {interval}s...")
                print("=" * 60)
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Monitoring stopped by user")
            print(f"📊 Stats: {scan_count} scans, {total_arbs} total arbs")

if __name__ == "__main__":
    detector = ArbitrageDetector()
    
    # Run monitoring loop (60 second interval)
    detector.monitor_loop(interval=60)
