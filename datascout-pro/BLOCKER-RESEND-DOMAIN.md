# 🚨 BLOCKER CRITIQUE - Resend Domain Verification

**Date**: 2026-04-26 16:05  
**Status**: BLOQUANT  
**Impact**: 0 emails envoyés, deadline revenue impossible à atteindre

---

## ❌ Problème

Tentative d'envoi de 5 cold emails batch 1 premium → **100% échec**

**Erreur Resend**:
```json
{
  "statusCode": 403,
  "message": "The datascout.pro domain is not verified. Please, add and verify your domain on https://resend.com/domains",
  "name": "validation_error"
}
```

**Root cause**: Le domaine `datascout.pro` n'est PAS vérifié dans le compte Resend.

---

## ✅ Solution (5-30 minutes)

### Étape 1: Login Resend
→ https://resend.com/login  
→ Login avec compte associé à `RESEND_API_KEY=re_bRV78NGE...`

### Étape 2: Add Domain
→ Dashboard > Domains > Add Domain  
→ Enter: `datascout.pro`

### Étape 3: Configure DNS
Resend va fournir des records DNS à ajouter chez le registrar (ex: OVH, Cloudflare, Namecheap).

**Records typiques** (à confirmer sur Resend dashboard):
- **TXT record** (SPF/DKIM): `v=spf1 include:resend.com ~all`
- **CNAME record** (DKIM): `resend._domainkey.datascout.pro` → `resend.com`
- **MX record** (optionnel pour receive): Priority 10 → `mx.resend.com`

### Étape 4: Wait Verification
- DNS propagation: 5-30 minutes
- Resend check automatique toutes les 5 min
- Status visible sur dashboard

### Étape 5: Re-test
```bash
cd /home/openclaw/.openclaw/workspace/datascout-pro
node send-batch-1-FIXED.js
```

---

## 🔧 Alternative Court-Terme (DEV ONLY)

**Utiliser Resend test email** (onboarding@resend.dev) pour tester l'infra.

⚠️ **NE PAS envoyer aux vrais prospects** avec `@resend.dev` (unprofessionnel).

Fichier: `send-batch-1-TEST.js` (déjà créé)

---

## 📊 Impact Business

| Métrique | Valeur |
|----------|--------|
| **Emails ready** | 5 premium prospects |
| **Emails sent** | 0 |
| **Emails failed** | 5 (100%) |
| **Revenue impact** | 0€ / 500€ objectif |
| **Time lost** | ~2h (scripting + debug) |
| **Time to fix** | 5-30 min (DNS config) |

---

## 🎯 Prochaine Étape

**Décision le J** :

1. **Option A (recommandée)** : Vérifier datascout.pro maintenant (30 min max)
   - Pro: Domaine propre, crédibilité, scaling futur
   - Cons: 30 min setup DNS

2. **Option B (backup)** : Utiliser autre domaine déjà vérifié
   - Si tu as un domaine perso/business vérifié sur Resend
   - Ex: `contact@tondomaine.fr` (avec reply-to datascout)

3. **Option C (last resort)** : Gmail/Outlook SMTP manuel
   - Moins professionnel
   - Risque spam filter
   - Pas de tracking opens/clicks

---

**Recommandation CEO** : Option A (30 min DNS config) pour débloquer tout le pipeline.

**Scripts prêts** :
- ✅ `send-batch-1-FIXED.js` (ready to execute après verification)
- ✅ 5 cold emails ultra-personnalisés (Kaviar House, Lazzaretti, Fossier, Transgourmet, Electrolux)
- ✅ Tracking system (tags, logs, revenue-tracking.json)

**Blocker actuel** : DNS uniquement. Tout le reste fonctionne.

---

**Fichiers générés** :
- `send-batch-1-premium.js` (DRY RUN - curl commands)
- `send-batch-1-premium-LIVE.js` (failed - tags error)
- `send-batch-1-FIXED.js` (failed - domain verification) ← **USE THIS**
- `prospection/batch-1-fixed-*.json` (execution logs)
