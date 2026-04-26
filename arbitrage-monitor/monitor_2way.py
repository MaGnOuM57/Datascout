#!/usr/bin/env python3
"""
Continuous monitor for 2-way sports arbitrage
Updates every 30 seconds with new opportunities
"""

import sys
import os

# Add parent directory to path to import scanner
sys.path.insert(0, os.path.dirname(__file__))

from real_arb_scanner import scan_for_arbitrage, format_opportunity, SPORTS_2WAY
import time
from datetime import datetime

def save_alert(opportunities):
    """Save latest opportunities to alert file"""
    if not opportunities:
        return
    
    alert_file = '/home/openclaw/.openclaw/workspace/arbitrage-monitor/alert_2way.txt'
    
    with open(alert_file, 'w') as f:
        f.write(f"🔍 Scan: {datetime.now().strftime('%H:%M:%S')}\n")
        f.write(f"📊 {len(opportunities)} opportunités trouvées\n\n")
        
        for i, opp in enumerate(opportunities[:3], 1):  # Top 3
            f.write(f"#{i}\n")
            f.write(format_opportunity(opp))
            f.write("\n" + "="*70 + "\n\n")
        
        f.write(f"\nGenerated: {datetime.now().isoformat()}\n")

def monitor_loop(interval: int = 30):
    """Continuous monitoring"""
    
    print("\n" + "="*70)
    print("🎯 ARBITRAGE MONITOR - SPORTS 2-WAY ONLY")
    print("="*70)
    print("\n✅ Sports monitorés:")
    for sport in SPORTS_2WAY.values():
        print(f"  • {sport}")
    print(f"\n🔄 Interval: {interval}s")
    print(f"💰 Seuil minimum: 1% profit")
    print()
    
    scan_count = 0
    total_found = 0
    
    try:
        while True:
            scan_count += 1
            
            print(f"\n{'='*70}")
            print(f"🔍 SCAN #{scan_count} - {datetime.now().strftime('%H:%M:%S')}")
            print('='*70)
            
            # Scan for opportunities
            opportunities = scan_for_arbitrage(use_real_api=False)
            
            if opportunities:
                total_found += len(opportunities)
                
                print(f"\n✅ {len(opportunities)} opportunités!\n")
                
                # Show top 3
                for i, opp in enumerate(opportunities[:3], 1):
                    event = opp['event']
                    arb = opp['arb']
                    
                    print(f"#{i} {event['sport']}: {event['player1']} vs {event['player2']}")
                    print(f"   💰 Profit: {arb['profit']}€ ({arb['profit_pct']}%)")
                    print(f"   📊 {event['bookmakers'][0]} @ {event['odds'][0]} + {event['bookmakers'][1]} @ {event['odds'][1]}")
                    print(f"   🕐 {event['time']}")
                    print()
                
                # Save for telegram pickup
                save_alert(opportunities)
                
            else:
                print("\n❌ Aucune opportunité ce scan")
            
            print(f"\n📊 Session: {total_found} opportunités total")
            print(f"⏰ Prochain scan dans {interval}s...")
            
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print(f"\n\n🛑 Monitoring arrêté")
        print(f"📊 Stats: {scan_count} scans, {total_found} opportunités")

if __name__ == "__main__":
    interval = 30
    
    if len(sys.argv) > 1:
        try:
            interval = int(sys.argv[1])
        except:
            pass
    
    monitor_loop(interval)
