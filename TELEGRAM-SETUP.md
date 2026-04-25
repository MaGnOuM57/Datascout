# 📱 Configuration Telegram - Guide Rapide

**Status actuel** : ❌ Telegram activé mais bot non connecté (token manquant)  
**Temps requis** : 5 minutes  
**Priorité** : 🔥 HAUTE (communication mobile essentielle)

---

## 🎯 Pourquoi Configurer Telegram ?

Avec Telegram configuré, tu pourras :
- ✅ Me parler depuis ton téléphone n'importe où
- ✅ Recevoir rapports quotidiens (22h) directement en DM
- ✅ Recevoir alertes business critiques instantanément
- ✅ Gérer le business en mobilité

Sans Telegram : Je ne peux que répondre via TUI (terminal uniquement).

---

## 📋 Étapes Configuration

### Étape 1 : Créer un Bot Telegram (2 min)

1. **Ouvre Telegram** sur ton téléphone/desktop
2. **Cherche** : `@BotFather` (bot officiel Telegram)
3. **Envoie** : `/newbot`
4. **Nom du bot** : `ApporteurCash AI` (ou ce que tu veux)
5. **Username du bot** : `apporteurcash_bot` (doit finir par `_bot`)
6. **Copie le token** : Tu reçois un message avec un token genre :
   ```
   123456789:ABCdefGHIjklMNOpqrsTUVwxyz1234567890
   ```
7. **GARDE CE TOKEN SECRET** ⚠️

### Étape 2 : Configurer OpenClaw (2 min)

#### Option A - Via CLI (recommandé) :

```bash
# Édite le fichier de config
nano ~/.openclaw/openclaw.json

# Trouve la section "channels" : "telegram" et ajoute :
{
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "TON_TOKEN_ICI",
      "dmPolicy": "pairing",
      "groupPolicy": "allowlist"
    }
  }
}

# Sauvegarde (Ctrl+O, Enter, Ctrl+X)
```

#### Option B - Via gateway.config.patch :

```bash
# Dans le TUI OpenClaw, demande-moi :
"Configure Telegram avec ce token : <TON_TOKEN>"
# Je vais utiliser gateway config.patch pour l'ajouter
```

### Étape 3 : Restart Gateway (30 sec)

```bash
openclaw gateway restart
```

Attends ~10 secondes que le gateway redémarre.

### Étape 4 : Pairing avec Ton Compte (1 min)

#### Option A - QR Code :
```bash
openclaw qr
```
Scanne le QR code avec ton téléphone → Ouvre Telegram → DM au bot.

#### Option B - Manuel :
1. Cherche ton bot dans Telegram : `@apporteurcash_bot`
2. Envoie `/start`
3. Le bot te demande un code de pairing
4. Dans le terminal :
   ```bash
   openclaw pairing pending
   openclaw pairing approve <request-id>
   ```

### Étape 5 : Test de Connexion

Dans Telegram, envoie au bot :
```
/status
```

Tu devrais recevoir une réponse avec infos session !

---

## ✅ Vérification

Une fois configuré, teste :

1. **Envoie un message** : `Salut, test Telegram`
2. **Demande status** : `/status`
3. **Test commande** : `Génère un rapport business DataScout Pro`

Si ça marche → **Telegram configuré ✅**

---

## 🔧 Troubleshooting

### Erreur "Unauthorized" ou "Invalid token"
→ Vérifie que tu as bien copié le token complet (sans espaces)

### Bot ne répond pas
→ Vérifie que le gateway est restart : `openclaw gateway status`

### "Pairing required"
→ Tu dois approuver le pairing : `openclaw pairing pending` puis `approve`

### Impossible de trouver le bot
→ Vérifie le username (doit finir par `_bot`)

---

## 📊 Configuration Avancée (Optionnel)

### Custom Commands (slash commands visibles)
```json
{
  "channels": {
    "telegram": {
      "customCommands": [
        {"command": "ventes", "description": "Check ventes DataScout Pro"},
        {"command": "prospects", "description": "Liste prospects contactés"},
        {"command": "rapport", "description": "Rapport business immédiat"}
      ]
    }
  }
}
```

### Groupes Telegram (si besoin)
```json
{
  "channels": {
    "telegram": {
      "groupPolicy": "allowlist",
      "groups": {
        "<group-id>": {
          "name": "Business Team",
          "allowFrom": ["*"]
        }
      }
    }
  }
}
```

---

## 🚀 Bénéfices Immédiats

Une fois Telegram configuré :

✅ **Rapports automatiques 22h chaque soir** (cron job déjà configuré)  
✅ **Alertes business critiques** en temps réel  
✅ **Gestion mobile** du business depuis n'importe où  
✅ **Heartbeats proactifs** si besoin d'attention  

---

**Status** : Prêt à configurer — Étapes 1-5 ci-dessus (5 min total)  
**Next** : Une fois configuré, réponds "Telegram OK ✅" pour que je teste la connexion

---

**Created** : 2026-04-25 10:48  
**Priority** : 🔥 HAUTE
