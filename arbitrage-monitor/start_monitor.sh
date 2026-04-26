#!/bin/bash
# Start continuous arbitrage monitoring

cd /home/openclaw/.openclaw/workspace/arbitrage-monitor

echo "🎯 ARBITRAGE MONITOR - DÉMARRAGE"
echo "================================"
echo ""
echo "📊 Scan interval: 120 secondes (2 min)"
echo "🎯 Min profit: 1%"
echo "📡 API: The Odds API (live)"
echo "💰 Capital: 500€"
echo ""
echo "Bookmakers actifs: TOUS"
echo "Sports: Tennis ATP/WTA, NBA, NHL, MLB, MMA"
echo ""
echo "Press Ctrl+C to stop"
echo ""

# Run monitor
python3 live_scanner.py 120
