# 🚀 DataScout Pro - Setup Autonomie Maximale

**Date** : 2026-04-25 14:05  
**Status** : Configuration en cours

---

## ✅ COMPLÉTÉ

### Infrastructure
- ✅ Vercel CLI installé (v52.0.0)
- ✅ GitHub remote configuré (https://github.com/MaGnOuM57/Datascout.git)
- ✅ Fichiers prêts à déployer (index.html + assets)

### Fichiers
- ✅ Landing page : `index.html` (9.9 KB) avec Stripe link
- ✅ Base prospects : 65 qualifiés (50 + 15)
- ✅ Templates emails : 3 variations prêtes
- ✅ Rapport exemple : PDF converti et prêt

---

## ⏳ EN ATTENTE : 2 Tokens Requis

### 1. GitHub Personal Access Token
**Pourquoi** : Push code vers repo  
**Obtention** (2 min) :
1. https://github.com/settings/tokens
2. "Generate new token (classic)"
3. Cocher : `repo` (full control of private repositories)
4. Copier le token

**Usage** : Une fois reçu, je configure git credentials et push immédiatement.

---

### 2. Vercel Token (Recommandé) OU GitHub OAuth
**Pourquoi** : Déployer automatiquement la landing page

**Option A : Vercel Token (Plus rapide, 2 min)**
1. https://vercel.com/account/tokens
2. "Create Token"
3. Name: "DataScout CLI"
4. Scope: Full Account
5. Copier le token

**Option B : GitHub OAuth (Alternative)**
- Je peux déployer via GitHub une fois le repo pushé
- Mais nécessite une auth Vercel via browser (moins autonome)

**Recommandation** : Vercel Token (Option A) pour autonomie maximale.

---

### 3. Resend API Key (Email Autonome)
**Pourquoi** : Envoi automatique emails prospection

**Obtention** (3 min) :
1. https://resend.com/signup
2. Créer compte (gratuit : 3000 emails/mois)
3. "API Keys" → "Create API Key"
4. Nom : "DataScout Prospection"
5. Permission : "Sending access"
6. Copier l'API key

**Alternative si compte email existant** :
- Gmail SMTP (app password)
- SendGrid
- Mailgun

**Recommandation** : Resend (le plus simple, gratuit, pas de config DNS requise au début).

---

## 🎯 UNE FOIS LES TOKENS REÇUS

### Séquence Automatique (5 min)
1. **GitHub** : Push code (30 sec)
2. **Vercel** : Deploy landing page (2 min)
3. **DNS** : Link custom domain si désiré (optionnel)
4. **Resend** : Configure envoi emails (1 min)
5. **Test** : Envoi email test (30 sec)
6. **Prospection** : Lance batch 10 premiers emails (1 min)

### Résultat Final
- ✅ Site live (URL fournie)
- ✅ Emails automatiques fonctionnels
- ✅ Prospection lancée (10 emails/jour)
- ✅ Tracking complet (rapports Telegram quotidiens)

---

## 📊 Après Setup : Business Loop Autonome

### Quotidien (Automatique)
- **9h-22h** : Heartbeat checks
- **10h, 14h, 18h** : Business execution (prospection)
- **22h** : Nightly report complet

### Actions Autonomes
- Recherche 10-15 nouveaux prospects/jour
- Envoi 10 emails/jour (personnalisés)
- Tracking ouvertures/réponses
- Update métriques
- Rapports Telegram

### Validation Requise
- Closer ventes (réponse prospects intéressés)
- Décisions >200€
- Changements stratégiques

---

## 🚨 NEXT : Envoie-moi les 3 Tokens

**Format** :
```
GitHub Token: ghp_xxxxxxxxxxxxx
Vercel Token: xxxxxxxxxxxxxxxxx
Resend API Key: re_xxxxxxxxxxxxx
```

Dès réception → Exécution complète en 5 minutes → Site live + prospection lancée.

---

**Créé** : 2026-04-25 14:05  
**Mode** : Autonomie Maximale CEO 🤖
