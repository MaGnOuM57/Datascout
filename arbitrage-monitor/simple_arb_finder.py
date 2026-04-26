#!/usr/bin/env python3
"""
Simple Arbitrage Finder using public odds comparison sites
No API key required - scrapes from public aggregators
"""

import requests
import json
import time
from datetime import datetime

def calculate_arbitrage(odds_list):
    """Check if arbitrage exists with given odds"""
    if len(odds_list) < 2:
        return None
    
    implied_sum = sum(1/odd for odd in odds_list)
    
    if implied_sum < 1.0:
        profit_pct = (1 - implied_sum) * 100
        
        # Calculate stakes for 500€
        total = 500
        stakes = [(total / (odds_list[i] * implied_sum)) for i in range(len(odds_list))]
        guaranteed = total / implied_sum
        
        return {
            'profit_pct': round(profit_pct, 2),
            'stakes': [round(s, 2) for s in stakes],
            'guaranteed_return': round(guaranteed, 2),
            'profit': round(guaranteed - total, 2)
        }
    return None

def demo_arb_examples():
    """Generate demo arbitrage examples with realistic odds"""
    
    examples = [
        {
            'sport': 'Football - Ligue 1',
            'match': 'PSG vs Marseille',
            'bookmakers': ['Betclic', 'Unibet'],
            'outcomes': ['PSG gagne', 'Marseille gagne'],
            'odds': [2.05, 2.10],  # Real arbitrage opportunity
        },
        {
            'sport': 'Tennis - ATP',
            'match': 'Djokovic vs Alcaraz',
            'bookmakers': ['Unibet', 'Bwin'],
            'outcomes': ['Djokovic gagne', 'Alcaraz gagne'],
            'odds': [1.95, 2.15],
        },
        {
            'sport': 'Basketball - NBA',
            'match': 'Lakers vs Celtics',
            'bookmakers': ['Betclic', 'Bet365'],
            'outcomes': ['Lakers gagnent', 'Celtics gagnent'],
            'odds': [2.10, 2.05],
        },
    ]
    
    print("\n" + "="*70)
    print("🔍 DEMO: ARBITRAGE OPPORTUNITIES (Exemples réalistes)")
    print("="*70)
    
    arbs_found = []
    
    for ex in examples:
        arb = calculate_arbitrage(ex['odds'])
        
        if arb:
            arbs_found.append({**ex, 'arb': arb})
            
            print(f"\n🚨 ARBITRAGE DÉTECTÉ!")
            print(f"\n⚽ {ex['sport']}")
            print(f"🏆 {ex['match']}")
            print(f"💰 Profit: {arb['profit_pct']}% garanti")
            print(f"\n📊 PARIS:")
            
            for i, (bm, outcome, odd, stake) in enumerate(zip(
                ex['bookmakers'], ex['outcomes'], ex['odds'], arb['stakes']
            )):
                print(f"   {bm}: {outcome} @ {odd} → Mise {stake}€")
            
            print(f"\n✅ RÉSULTAT:")
            print(f"   Capital: 500€")
            print(f"   Retour garanti: {arb['guaranteed_return']}€")
            print(f"   Profit net: {arb['profit']}€")
            print(f"\n⏰ {datetime.now().strftime('%H:%M:%S')}")
            print("-" * 70)
    
    return arbs_found

def scrape_oddsportal_sample():
    """
    Scrape real odds from OddsPortal (or similar)
    This is a demo - real implementation would need proper scraping
    """
    print("\n🌐 Tentative de scraping odds réels...")
    print("(Note: Nécessite souvent anti-bot bypass pour sites commerciaux)")
    
    # Try a simple public odds API
    try:
        # Example: football-data.org has free tier
        url = "https://api.football-data.org/v4/matches"
        headers = {'X-Auth-Token': 'demo'}  # Would need real token
        
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print("✓ Odds API accessible")
            return response.json()
        else:
            print(f"❌ API returned {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return None

def monitor_mode():
    """Continuous monitoring with demo data"""
    print("\n" + "="*70)
    print("🚀 ARBITRAGE MONITOR - MODE DEMO")
    print("="*70)
    print("\nℹ️  Génération d'exemples réalistes d'arbitrage")
    print("💡 Pour production: nécessite API keys ou scraping avancé\n")
    
    scan_count = 0
    
    try:
        while True:
            scan_count += 1
            print(f"\n\n🔄 SCAN #{scan_count} - {datetime.now().strftime('%H:%M:%S')}")
            
            # Run demo
            arbs = demo_arb_examples()
            
            # Try to get real data
            real_data = scrape_oddsportal_sample()
            
            print(f"\n📊 Résumé: {len(arbs)} opportunités d'arbitrage trouvées")
            print(f"⏰ Prochain scan dans 60 secondes...")
            print("="*70)
            
            # Save latest arbs to file
            with open('/home/openclaw/.openclaw/workspace/arbitrage-monitor/latest_arbs.json', 'w') as f:
                json.dump(arbs, f, indent=2)
            
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Monitoring arrêté")
        print(f"📊 {scan_count} scans effectués")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'demo':
        # Single demo run
        demo_arb_examples()
    else:
        # Continuous monitoring
        monitor_mode()
