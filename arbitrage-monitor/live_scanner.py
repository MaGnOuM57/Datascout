#!/usr/bin/env python3
"""
Live arbitrage scanner using The Odds API
Real odds, real opportunities
"""

import requests
import json
import time
from datetime import datetime
from typing import List, Dict, Optional

API_KEY = "8f958673d736aaed4e2c68cb69342b1b"
BASE_URL = "https://api.the-odds-api.com/v4"

# Sports with 2 outcomes only (no draw)
SPORTS_2WAY = {
    'tennis_atp_madrid_open': 'Tennis ATP Madrid',
    'tennis_wta_madrid_open': 'Tennis WTA Madrid',
    'basketball_nba': 'NBA',
    'icehockey_nhl': 'NHL',
    'baseball_mlb': 'MLB',
    'mma_mixed_martial_arts': 'MMA/UFC',
}

# EU bookmakers - Accept ALL available
# User will create accounts as needed
TARGET_BOOKMAKERS = None  # None = accept all bookmakers

def get_odds(sport_key: str) -> Optional[List[Dict]]:
    """Fetch live odds for a sport"""
    
    url = f"{BASE_URL}/sports/{sport_key}/odds"
    params = {
        'apiKey': API_KEY,
        'regions': 'eu',
        'markets': 'h2h',
        'oddsFormat': 'decimal',
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"  ✗ {sport_key}: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"  ✗ {sport_key}: {e}")
    
    return None

def calculate_arbitrage(odds1: float, odds2: float) -> Dict:
    """Calculate if arbitrage exists"""
    
    implied_prob = (1/odds1) + (1/odds2)
    
    if implied_prob < 1.0:
        # Arbitrage exists!
        profit_pct = ((1 - implied_prob) * 100)
        
        # Calculate optimal stakes for 500€ capital
        capital = 500
        stake1 = capital / (1 + (odds1/odds2))
        stake2 = capital - stake1
        
        # Guaranteed return
        return_amount = min(stake1 * odds1, stake2 * odds2)
        profit = return_amount - capital
        
        return {
            'exists': True,
            'profit_pct': round(profit_pct, 2),
            'profit': round(profit, 2),
            'stake1': round(stake1, 2),
            'stake2': round(stake2, 2),
            'return': round(return_amount, 2),
        }
    
    return {'exists': False}

def find_arbitrages(events: List[Dict], sport_name: str) -> List[Dict]:
    """Find arbitrage opportunities in events"""
    
    opportunities = []
    
    for event in events:
        home_team = event.get('home_team', '')
        away_team = event.get('away_team', '')
        commence_time = event.get('commence_time', '')
        
        bookmakers = event.get('bookmakers', [])
        
        # Collect all odds for this match
        odds_by_bookmaker = {}
        
        for bookmaker in bookmakers:
            book_key = bookmaker.get('key', '')
            title = bookmaker.get('title', book_key)
            
            # Accept all bookmakers (no filter)
            # if TARGET_BOOKMAKERS and book_key not in TARGET_BOOKMAKERS:
            #     continue
            
            markets = bookmaker.get('markets', [])
            for market in markets:
                if market.get('key') == 'h2h':
                    outcomes = market.get('outcomes', [])
                    
                    if len(outcomes) == 2:
                        # Store odds
                        odds_by_bookmaker[book_key] = {
                            'outcome1': outcomes[0].get('name'),
                            'odds1': outcomes[0].get('price'),
                            'outcome2': outcomes[1].get('name'),
                            'odds2': outcomes[1].get('price'),
                        }
        
        # Now find best combination
        if len(odds_by_bookmaker) >= 2:
            bookies = list(odds_by_bookmaker.keys())
            
            for i, bookie1 in enumerate(bookies):
                for bookie2 in bookies[i+1:]:
                    
                    odds1_data = odds_by_bookmaker[bookie1]
                    odds2_data = odds_by_bookmaker[bookie2]
                    
                    # Try both combinations
                    combinations = [
                        (odds1_data['odds1'], odds2_data['odds2'], 
                         odds1_data['outcome1'], odds2_data['outcome2'],
                         bookie1, bookie2),
                        (odds1_data['odds2'], odds2_data['odds1'],
                         odds1_data['outcome2'], odds2_data['outcome1'],
                         bookie1, bookie2),
                    ]
                    
                    for odds1, odds2, outcome1, outcome2, book1, book2 in combinations:
                        arb = calculate_arbitrage(odds1, odds2)
                        
                        if arb['exists'] and arb['profit_pct'] >= 1.0:
                            opportunities.append({
                                'sport': sport_name,
                                'event': f"{home_team} vs {away_team}",
                                'time': commence_time,
                                'outcome1': outcome1,
                                'outcome2': outcome2,
                                'bookmaker1': book1,
                                'odds1': odds1,
                                'bookmaker2': book2,
                                'odds2': odds2,
                                'arb': arb,
                            })
    
    return opportunities

def format_telegram_alert(opp: Dict) -> str:
    """Format opportunity for Telegram"""
    
    arb = opp['arb']
    time_str = opp['time'][:16].replace('T', ' ')
    
    # Determine sport emoji
    sport_emoji = '⚽'
    if 'Tennis' in opp['sport']:
        sport_emoji = '🎾'
    elif 'NBA' in opp['sport']:
        sport_emoji = '🏀'
    elif 'NHL' in opp['sport']:
        sport_emoji = '🏒'
    elif 'MMA' in opp['sport']:
        sport_emoji = '🥊'
    elif 'MLB' in opp['sport']:
        sport_emoji = '⚾'
    
    msg = f"""🚨 **ARBITRAGE DÉTECTÉ!**

{sport_emoji} **{opp['sport']}**
🏆 {opp['event']}

💰 **Profit: {arb['profit']}€ ({arb['profit_pct']}%)**

📊 **PARIS:**
{opp['bookmaker1'].upper()}: {opp['outcome1']} @ {opp['odds1']} → {arb['stake1']}€
{opp['bookmaker2'].upper()}: {opp['outcome2']} @ {opp['odds2']} → {arb['stake2']}€

✅ **RÉSULTAT GARANTI:**
Capital: 500€
Retour: {arb['return']}€
Profit net: {arb['profit']}€

⏰ Match: {time_str}
"""
    
    return msg

def send_telegram_alert(message: str):
    """Send alert to Telegram"""
    try:
        # Use openclaw message tool would go here
        # For now, save to file for pickup
        with open('alert_live.txt', 'w') as f:
            f.write(message)
            f.write(f"\n\nTimestamp: {datetime.now().isoformat()}\n")
        
        print("\n" + "="*70)
        print(message)
        print("="*70)
        
    except Exception as e:
        print(f"Alert error: {e}")

def scan_all_sports() -> List[Dict]:
    """Scan all 2-way sports for arbitrages"""
    
    all_opportunities = []
    
    print(f"\n🔍 SCAN LIVE - {datetime.now().strftime('%H:%M:%S')}")
    print("="*70)
    
    for sport_key, sport_name in SPORTS_2WAY.items():
        print(f"\n{sport_name}...", end=' ', flush=True)
        
        events = get_odds(sport_key)
        
        if events:
            print(f"{len(events)} events", end=' ')
            
            opportunities = find_arbitrages(events, sport_name)
            
            if opportunities:
                print(f"→ ✅ {len(opportunities)} arbitrages!")
                all_opportunities.extend(opportunities)
            else:
                print("→ ❌ no arb")
        else:
            print("→ ✗ no data")
        
        # Small delay between API calls
        time.sleep(0.5)
    
    return all_opportunities

def monitor_continuous(interval_seconds: int = 120):
    """Continuous monitoring loop"""
    
    print("\n" + "="*70)
    print("🎯 LIVE ARBITRAGE MONITOR - REAL ODDS")
    print("="*70)
    print(f"\n💰 Capital: 500€")
    print(f"📊 Sports: {', '.join(SPORTS_2WAY.values())}")
    print(f"🔄 Interval: {interval_seconds}s")
    print(f"🎯 Min profit: 1%")
    print(f"📡 API: The Odds API (live)")
    print()
    
    scan_count = 0
    total_found = 0
    best_profit = 0
    
    try:
        while True:
            scan_count += 1
            
            opportunities = scan_all_sports()
            
            if opportunities:
                # Sort by profit
                opportunities.sort(key=lambda x: x['arb']['profit_pct'], reverse=True)
                
                total_found += len(opportunities)
                
                # Send alert for best one
                best = opportunities[0]
                best_profit = max(best_profit, best['arb']['profit_pct'])
                
                alert_msg = format_telegram_alert(best)
                send_telegram_alert(alert_msg)
                
                # Save all to file
                with open('opportunities_live.json', 'w') as f:
                    json.dump(opportunities, f, indent=2)
                
                print(f"\n💾 {len(opportunities)} opportunités sauvegardées")
            else:
                print(f"\n❌ Aucune opportunité ce scan")
            
            print(f"\n📊 Session stats:")
            print(f"  • Scans: {scan_count}")
            print(f"  • Total found: {total_found}")
            print(f"  • Best profit: {best_profit}%")
            print(f"\n⏰ Prochain scan dans {interval_seconds}s...\n")
            
            time.sleep(interval_seconds)
    
    except KeyboardInterrupt:
        print(f"\n\n🛑 Monitoring arrêté")
        print(f"📊 Final stats: {scan_count} scans, {total_found} opportunités")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--once':
        # Single scan
        opportunities = scan_all_sports()
        
        if opportunities:
            opportunities.sort(key=lambda x: x['arb']['profit_pct'], reverse=True)
            
            print(f"\n\n✅ {len(opportunities)} ARBITRAGES TROUVÉS!\n")
            
            for i, opp in enumerate(opportunities[:5], 1):
                print(f"#{i}")
                print(format_telegram_alert(opp))
                print()
        else:
            print(f"\n\n❌ Aucun arbitrage trouvé ce scan")
    else:
        # Continuous monitoring
        interval = 120  # 2 minutes default
        if len(sys.argv) > 1:
            try:
                interval = int(sys.argv[1])
            except:
                pass
        
        monitor_continuous(interval)
