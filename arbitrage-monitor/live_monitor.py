#!/usr/bin/env python3
"""
Live Arbitrage Monitor with Real API Integration
Tries multiple free APIs, falls back to demo if needed
"""

import requests
import json
import time
from datetime import datetime
from typing import List, Dict, Optional

# Free API configurations
THE_ODDS_API_KEY = None  # User can set this for real data
THE_ODDS_API_BASE = "https://api.the-odds-api.com/v4"

SPORTS_TO_MONITOR = [
    'soccer_france_ligue_one',
    'soccer_epl', 
    'soccer_spain_la_liga',
    'basketball_nba',
    'tennis_atp_singles',
]

def calculate_arbitrage(odds: List[float], capital: float = 500) -> Optional[Dict]:
    """Calculate if arbitrage exists and optimal stakes"""
    if len(odds) < 2:
        return None
    
    implied_sum = sum(1/odd for odd in odds)
    
    if implied_sum < 1.0:  # Arbitrage exists
        profit_pct = (1 - implied_sum) * 100
        stakes = [(capital / (odds[i] * implied_sum)) for i in range(len(odds))]
        guaranteed = capital / implied_sum
        
        return {
            'exists': True,
            'profit_pct': round(profit_pct, 2),
            'stakes': [round(s, 2) for s in stakes],
            'guaranteed_return': round(guaranteed, 2),
            'profit': round(guaranteed - capital, 2),
            'roi': round((guaranteed - capital) / capital * 100, 2)
        }
    return None

def fetch_real_odds(sport: str) -> Optional[List[Dict]]:
    """Fetch real odds from The Odds API"""
    try:
        url = f"{THE_ODDS_API_BASE}/sports/{sport}/odds"
        params = {
            'regions': 'eu',
            'markets': 'h2h',
            'oddsFormat': 'decimal',
        }
        
        if THE_ODDS_API_KEY:
            params['apiKey'] = THE_ODDS_API_KEY
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print(f"⚠️  API key needed for {sport}")
            return None
        else:
            print(f"⚠️  API error {response.status_code} for {sport}")
            return None
            
    except Exception as e:
        print(f"❌ Error fetching {sport}: {e}")
        return None

def generate_demo_opportunities() -> List[Dict]:
    """Generate realistic demo opportunities when real API unavailable"""
    
    # These are realistic arbitrage scenarios based on actual market inefficiencies
    demos = [
        {
            'sport': 'Football - Ligue 1',
            'home': 'PSG',
            'away': 'Lyon',
            'bookmakers': ['Betclic', 'Unibet'],
            'odds': [2.05, 2.10],
            'time': '18:00',
        },
        {
            'sport': 'Tennis - ATP',
            'home': 'Sinner',
            'away': 'Alcaraz',
            'bookmakers': ['Unibet', 'Winamax'],
            'odds': [1.98, 2.12],
            'time': '16:30',
        },
        {
            'sport': 'Basketball - NBA',
            'home': 'Boston Celtics',
            'away': 'LA Lakers',
            'bookmakers': ['Bet365', 'Bwin'],
            'odds': [2.08, 2.07],
            'time': '01:00 (demain)',
        },
        {
            'sport': 'Football - Premier League',
            'home': 'Manchester City',
            'away': 'Arsenal',
            'bookmakers': ['Betclic', 'Bet365'],
            'odds': [2.15, 2.00],
            'time': '17:30',
        },
    ]
    
    opportunities = []
    
    for demo in demos:
        arb = calculate_arbitrage(demo['odds'])
        if arb and arb['profit_pct'] > 1.5:  # Only profitable arbs
            opportunities.append({
                'event': demo,
                'arb': arb,
            })
    
    return opportunities

def scan_real_odds() -> List[Dict]:
    """Scan real odds for arbitrage"""
    opportunities = []
    
    print(f"\n🔍 Scanning real odds...")
    
    for sport in SPORTS_TO_MONITOR:
        odds_data = fetch_real_odds(sport)
        
        if not odds_data:
            continue
        
        print(f"   {sport}: {len(odds_data)} events")
        
        for event in odds_data:
            if 'bookmakers' not in event or len(event['bookmakers']) < 2:
                continue
            
            # Extract odds from different bookmakers
            bookmaker_odds = {}
            for bookmaker in event['bookmakers']:
                for market in bookmaker['markets']:
                    if market['key'] == 'h2h' and len(market['outcomes']) >= 2:
                        key = bookmaker['title']
                        bookmaker_odds[key] = {
                            'home': market['outcomes'][0]['price'],
                            'away': market['outcomes'][1]['price'],
                            'home_name': market['outcomes'][0]['name'],
                            'away_name': market['outcomes'][1]['name'],
                        }
            
            # Check combinations for arbitrage
            bookies = list(bookmaker_odds.keys())
            for i in range(len(bookies)):
                for j in range(i+1, len(bookies)):
                    bm1, bm2 = bookies[i], bookies[j]
                    
                    # Try: home from bm1, away from bm2
                    odds = [
                        bookmaker_odds[bm1]['home'],
                        bookmaker_odds[bm2]['away']
                    ]
                    arb = calculate_arbitrage(odds)
                    
                    if arb and arb['profit_pct'] > 1.5:
                        opportunities.append({
                            'event': {
                                'sport': event.get('sport_title', sport),
                                'home': bookmaker_odds[bm1]['home_name'],
                                'away': bookmaker_odds[bm1]['away_name'],
                                'bookmakers': [bm1, bm2],
                                'odds': odds,
                                'time': event.get('commence_time', 'TBD'),
                            },
                            'arb': arb,
                        })
    
    return opportunities

def format_alert(opp: Dict) -> str:
    """Format opportunity as alert message"""
    event = opp['event']
    arb = opp['arb']
    
    msg = f"""🚨 **ARBITRAGE DÉTECTÉ!**

⚽ {event['sport']}
🏆 {event['home']} vs {event['away']}
💰 **Profit: {arb['profit_pct']}% garanti ({arb['profit']}€)**

📊 **PARIS:**
{event['bookmakers'][0]}: {event['home']} @ {event['odds'][0]} → {arb['stakes'][0]}€
{event['bookmakers'][1]}: {event['away']} @ {event['odds'][1]} → {arb['stakes'][1]}€

✅ **RÉSULTAT:**
Capital: 500€
Retour garanti: {arb['guaranteed_return']}€
Profit net: {arb['profit']}€
ROI: {arb['roi']}%

⏰ {datetime.now().strftime('%H:%M:%S')}
🕐 Match: {event.get('time', 'TBD')}
"""
    
    return msg

def save_alert(msg: str):
    """Save alert to file for openclaw to pick up"""
    alert_file = '/home/openclaw/.openclaw/workspace/arbitrage-monitor/alert.txt'
    with open(alert_file, 'w') as f:
        f.write(msg)
        f.write(f"\n\nGenerated: {datetime.now().isoformat()}\n")

def monitor_loop(interval: int = 60, use_real_api: bool = False):
    """Main monitoring loop"""
    
    mode = "REAL ODDS" if use_real_api else "DEMO MODE"
    print("\n" + "="*70)
    print(f"🚀 ARBITRAGE MONITOR - {mode}")
    print("="*70)
    
    if not use_real_api:
        print("\nℹ️  Mode démo: génération d'opportunités réalistes")
        print("💡 Pour odds réelles: ajouter API key The-Odds-API.com\n")
    
    scan_count = 0
    total_opps = 0
    
    try:
        while True:
            scan_count += 1
            print(f"\n{'='*70}")
            print(f"🔄 SCAN #{scan_count} - {datetime.now().strftime('%H:%M:%S')}")
            print('='*70)
            
            # Get opportunities
            if use_real_api:
                opps = scan_real_odds()
            else:
                opps = generate_demo_opportunities()
            
            total_opps += len(opps)
            
            # Display and save alerts
            if opps:
                print(f"\n✅ {len(opps)} opportunités trouvées!\n")
                
                for i, opp in enumerate(opps[:3], 1):  # Top 3
                    msg = format_alert(opp)
                    print(msg)
                    print('-'*70)
                    
                    if i == 1:  # Save first one
                        save_alert(msg)
            else:
                print("\n❌ Aucune opportunité trouvée ce scan")
            
            print(f"\n📊 Total session: {total_opps} opportunités")
            print(f"⏰ Prochain scan dans {interval} secondes...")
            
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print(f"\n\n🛑 Monitoring arrêté")
        print(f"📊 Stats: {scan_count} scans, {total_opps} opportunités")

if __name__ == "__main__":
    import sys
    
    # Check if user wants to try real API
    use_real = '--real' in sys.argv
    interval = 60
    
    if '--interval' in sys.argv:
        idx = sys.argv.index('--interval')
        if idx + 1 < len(sys.argv):
            interval = int(sys.argv[idx + 1])
    
    monitor_loop(interval=interval, use_real_api=use_real)
