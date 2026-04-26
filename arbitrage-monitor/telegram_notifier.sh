#!/bin/bash
# Watch for alert file changes and send to Telegram

ALERT_FILE="/home/openclaw/.openclaw/workspace/arbitrage-monitor/alert.txt"
LAST_ALERT=""

echo "📢 Telegram Notifier Started"
echo "Watching: $ALERT_FILE"

while true; do
    if [ -f "$ALERT_FILE" ]; then
        CURRENT=$(cat "$ALERT_FILE")
        
        if [ "$CURRENT" != "$LAST_ALERT" ] && [ -n "$CURRENT" ]; then
            echo "🚨 New alert detected!"
            
            # Save to notification queue for openclaw
            echo "$CURRENT" > /home/openclaw/.openclaw/workspace/arbitrage-monitor/pending_notification.txt
            
            LAST_ALERT="$CURRENT"
        fi
    fi
    
    sleep 5
done
