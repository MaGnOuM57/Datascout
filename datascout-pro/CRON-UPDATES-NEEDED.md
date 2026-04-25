# Cron Jobs Updates - Mode Revenu Maximal

## Commandes à exécuter (User)

### 1. Heartbeat - Passer à 30 min

```bash
# Supprimer ancien heartbeat (1h)
openclaw cron remove f47ec49b-f678-45d5-97cb-9bb2cf1b73dd

# Créer nouveau heartbeat (30 min)
openclaw cron add \
  --schedule "*/30 9-22 * * *" \
  --task "Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK." \
  --label "Heartbeat Proactif CEO - 30 min" \
  --model anthropic/claude-haiku-3-5 \
  --delivery telegram \
  --timezone Europe/Berlin
```

### 2. Business Execution - Ajouter slot 21h

```bash
# Ajouter nouveau slot 21h
openclaw cron add \
  --schedule "0 21 * * *" \
  --task "Execute autonomous business tasks: prospection, email sending, sales tracking, optimizations. Focus on 500€ revenue objective. Update revenue-tracking.json." \
  --label "Revenue Execution 21h" \
  --model anthropic/claude-sonnet-4-5 \
  --delivery telegram \
  --timezone Europe/Berlin
```

### 3. Revenue Reports - Toutes les 6h

```bash
# Report 12h
openclaw cron add \
  --schedule "0 12 * * *" \
  --task "Send revenue report to Telegram: sales today, emails sent, conversion rates, next actions." \
  --label "Revenue Report Midi" \
  --model anthropic/claude-haiku-3-5 \
  --delivery telegram \
  --timezone Europe/Berlin

# Report 18h
openclaw cron add \
  --schedule "0 18 * * *" \
  --task "Send revenue report to Telegram: sales today, emails sent, conversion rates, next actions." \
  --label "Revenue Report Soir" \
  --model anthropic/claude-haiku-3-5 \
  --delivery telegram \
  --timezone Europe/Berlin
```

---

**Note**: Le nightly report 22h existe déjà, pas besoin de le recréer.
