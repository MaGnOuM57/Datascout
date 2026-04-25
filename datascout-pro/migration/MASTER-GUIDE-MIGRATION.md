# 🚀 GUIDE COMPLET MIGRATION ellievai.com

**Durée totale**: 30 minutes (hors propagation DNS)

---

## 📋 CHECKLIST GLOBALE

- [ ] **Étape 1**: Config DNS OVH (10 min)
- [ ] **Étape 2**: Config Vercel domaine (5 min)
- [ ] **Étape 3**: Vérification déploiement (5 min)
- [ ] **Étape 4**: Config Resend email (5 min)
- [ ] **Étape 5**: Tests finaux (5 min)

**⏱️ Temps d'attente**: 5-30 min propagation DNS (automatique)

---

## 🎯 ÉTAPE 1: CONFIGURATION DNS OVH (10 min)

### Connexion OVH

1. Va sur: https://www.ovh.com/manager/
2. **Web Cloud** → **Noms de domaine** → **ellievai.com**
3. Onglet **Zone DNS**

---

### Records à Ajouter (6 records)

#### ✉️ EMAIL - Record 1: MX
```
Type: MX
Sous-domaine: (vide) ou @
Cible: feedback-smtp.eu-west-1.amazonses.com
Priorité: 10
TTL: 3600
```

**Comment faire dans OVH**:
- Clique **Ajouter une entrée**
- Choisis **MX**
- Laisse "Sous-domaine" vide (ou tape `@`)
- Colle la cible
- Priorité = 10
- **Ajouter**

---

#### ✉️ EMAIL - Record 2: SPF
```
Type: TXT
Sous-domaine: (vide) ou @
Valeur: v=spf1 include:amazonses.com ~all
TTL: 3600
```

**⚠️ IMPORTANT**: Si tu as déjà un record SPF existant:
- **SUPPRIME l'ancien** (ne garde qu'un seul SPF)
- Remplace par le nouveau

---

#### ✉️ EMAIL - Record 3: DKIM
```
Type: TXT
Sous-domaine: resend._domainkey
Valeur: p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDe+glSbi2aTCB3EHLS99SYeJ0/BQYIZEGgppKPEem2k0RXKQfZIX0GcTUnxN3sW9d1dQ/bnYK0QR6z4DDiz0hdWcRp4FLRGmIlC3Y7E1xqSVn79pva7bp17Tu6o9EC3s+x8XQq0Que/clG3wyFIs7hapTK3+TWzOvqkXD7ZhBGQQIDAQAB
TTL: 3600
```

**⚠️ ATTENTION**: Dans le champ "Sous-domaine", tape exactement:
```
resend._domainkey
```

(Pas de point, pas d'espace)

---

#### ✉️ EMAIL - Record 4: DMARC
```
Type: TXT
Sous-domaine: _dmarc
Valeur: v=DMARC1; p=quarantine; rua=mailto:contact@ellievai.com; pct=100; adkim=s; aspf=s
TTL: 3600
```

---

#### 🌐 VERCEL - Record 5: CNAME www
```
Type: CNAME
Sous-domaine: www
Cible: cname.vercel-dns.com.
TTL: 3600
```

**⚠️ IMPORTANT**: Le point final (.) après `.com` est nécessaire:
```
cname.vercel-dns.com.
```

---

#### 🌐 VERCEL - Record 6: A (racine)
```
Type: A
Sous-domaine: (vide) ou @
Cible: 76.76.21.21
TTL: 3600
```

**Alternative (si OVH propose ALIAS)**:
```
Type: ALIAS ou ANAME
Sous-domaine: @
Cible: cname.vercel-dns.com
```

(Utilise A sinon)

---

### ✅ Validation OVH

Après avoir ajouté les 6 records:
1. Clique **Enregistrer** (si nécessaire)
2. OVH affiche "Configuration en cours"
3. **Attends 5-30 min** (propagation DNS)

**📸 Screenshot recommandé**: Capture l'onglet Zone DNS avec tous les records visibles.

---

### 🔍 Vérification propagation (après 5-30 min)

**Via terminal** (si dispo):
```bash
# SPF
dig TXT ellievai.com +short

# DKIM
dig TXT resend._domainkey.ellievai.com +short

# DMARC
dig TXT _dmarc.ellievai.com +short

# MX
dig MX ellievai.com +short

# Vercel
dig ellievai.com +short
dig www.ellievai.com +short
```

**Via web**:
- https://mxtoolbox.com/SuperTool.aspx (tape `ellievai.com`)
- Vérifie que SPF, DKIM, DMARC sont verts (✅)

---

## 🎯 ÉTAPE 2: CONFIGURATION VERCEL (5 min)

### 1. Connexion Vercel

Va sur: https://vercel.com/dashboard

Trouve ton projet: **datascout-pro** (ou nom actuel)

---

### 2. Ajouter ellievai.com

1. Clique sur le projet
2. **Settings** (onglet en haut)
3. Scroll jusqu'à **Domains**
4. Clique **Add**
5. Entre: `ellievai.com`
6. Clique **Add**

Vercel affiche:
- ⏳ **Pending**: DNS pas encore propagé (normal, attends 5-30 min)
- ✅ **Valid**: DNS OK, domaine configuré

---

### 3. Ajouter www.ellievai.com

Répète l'étape 2 avec: `www.ellievai.com`

Vercel va auto-rediriger www → ellievai.com (ou inverse selon config).

---

### 4. SSL Automatique

Vercel génère automatiquement un certificat SSL (Let's Encrypt).

**Temps**: 1-5 min après validation domaine.

Tu verras dans Domains:
- 🔒 **SSL Certificate**: Active

---

### ✅ Validation Vercel

Après ajout des 2 domaines:
1. Vérifie status = **Valid** (✅ vert)
2. Vérifie SSL = **Active** (🔒)

**Si "Pending"**: Attends 10-30 min (DNS pas encore propagé).

---

## 🎯 ÉTAPE 3: VÉRIFICATION DÉPLOIEMENT (5 min)

### Test Site Live

1. Va sur: https://ellievai.com
2. Vérifie que le site s'affiche correctement
3. Vérifie HTTPS (cadenas vert 🔒 dans navigateur)
4. Vérifie www: https://www.ellievai.com (doit rediriger vers ellievai.com)

---

### Checklist Visuelle

- [ ] Logo/Nom = "Ellie VAI" (pas "DataScout Pro")
- [ ] Email footer = contact@ellievai.com
- [ ] Liens = ellievai.com (pas datascout-pro.vercel.app)
- [ ] HTTPS actif (cadenas vert)
- [ ] Mobile responsive (teste sur téléphone)

---

### Test Pages Produits

- https://ellievai.com/vege.html
- https://ellievai.com/boutiques.html
- https://ellievai.com/caves.html

Vérifie que toutes affichent "Ellie VAI" et le bon domaine.

---

## 🎯 ÉTAPE 4: CONFIGURATION RESEND EMAIL (5 min)

### 1. Connexion Resend

Va sur: https://resend.com/domains

---

### 2. Vérifier domaine

Si tu as déjà ajouté `ellievai.com`:
1. Check status = **Verified** (✅ vert)
2. Si "Pending", attends propagation DNS (5-30 min)
3. Si toujours pending après 30 min, clique **Verify** manuellement

Si pas encore ajouté:
1. Clique **Add Domain**
2. Entre: `ellievai.com`
3. Resend affiche les DNS records (déjà configurés à l'étape 1)
4. Attends status **Verified**

---

### 3. Test Email

Envoie un email test pour vérifier délivrabilité:

**Option 1 - Via Resend Dashboard**:
1. Va sur https://resend.com/emails
2. Clique **Send Email**
3. From: `contact@ellievai.com`
4. To: ton email perso
5. Subject: "Test Ellie VAI"
6. Body: "Test de délivrabilité"
7. **Send**

**Option 2 - Via mail-tester.com**:
1. Va sur https://www.mail-tester.com
2. Copie l'adresse test affichée
3. Envoie un email depuis Resend vers cette adresse
4. Clique **Check Score**
5. **Target**: Score ≥ 9/10

---

### ✅ Validation Email

- [ ] Email reçu en inbox (pas spam)
- [ ] From = contact@ellievai.com
- [ ] Score mail-tester ≥ 9/10 (si testé)
- [ ] Resend status = Verified (✅)

---

## 🎯 ÉTAPE 5: TESTS FINAUX (5 min)

### Checklist Complète

#### DNS
- [ ] SPF propagé (vérifié via mxtoolbox.com)
- [ ] DKIM propagé
- [ ] DMARC propagé
- [ ] MX propagé
- [ ] A record pointe vers Vercel

#### Site
- [ ] https://ellievai.com fonctionne
- [ ] https://www.ellievai.com redirige
- [ ] SSL actif (cadenas vert)
- [ ] Branding = "Ellie VAI" partout
- [ ] Email = contact@ellievai.com partout
- [ ] Mobile responsive

#### Email
- [ ] Resend domaine verified
- [ ] Email test reçu
- [ ] Inbox (pas spam)
- [ ] Score mail-tester ≥ 9/10

---

### Test Complet Prospection

Lance un test d'envoi batch 1 (5 emails):

```bash
cd ~/workspace/datascout-pro/prospection
python3 send-batch-safe.py batch-1-ultra-qualified.json --dry-run
```

Vérifie dans le preview:
- [ ] From = "Ellie VAI <contact@ellievai.com>"
- [ ] Lien = https://ellievai.com
- [ ] Pas de mention "DataScout"

Si OK:
```bash
python3 send-batch-safe.py batch-1-ultra-qualified.json
```

(Envoi réel, durée 15-25 min)

---

## 🚨 PROBLÈMES COURANTS

### DNS pas propagé après 30 min
**Symptômes**: Vercel status = "Invalid Configuration" OU Resend = "Pending"

**Solutions**:
1. Vérifie records OVH (typos?)
2. Force refresh DNS local: `sudo systemd-resolve --flush-caches` (Linux)
3. Teste avec autre DNS: https://dnschecker.org/#A/ellievai.com
4. Attends jusqu'à 2h max (OVH parfois lent)

---

### Emails vont en spam
**Symptômes**: Email test arrive en spam folder

**Solutions**:
1. Vérifie DMARC configuré (record 4)
2. Vérifie SPF (record 2)
3. Teste mail-tester.com (score doit être ≥9/10)
4. Attends 24h (warm-up domaine)
5. Envoie batch 1 progressivement (pas 50 d'un coup)

---

### Site affiche "404 Not Found"
**Symptômes**: ellievai.com ne charge pas

**Solutions**:
1. Vérifie Vercel Domains status (doit être "Valid" ✅)
2. Vérifie record A dans OVH (76.76.21.21)
3. Attends propagation (5-30 min)
4. Force rebuild Vercel: Settings → Deployments → dernier deploy → Redeploy

---

### SSL "Not Secure"
**Symptômes**: Navigateur affiche "Non sécurisé"

**Solutions**:
1. Vercel génère SSL auto (attends 5 min)
2. Force HTTPS: Vercel Settings → Force HTTPS Redirect = ON
3. Clear cache navigateur (Ctrl+Shift+R)

---

## ✅ VALIDATION FINALE

**Tout est OK si**:
- ✅ https://ellievai.com charge en HTTPS
- ✅ Branding = "Ellie VAI" partout
- ✅ Email test reçu en inbox
- ✅ Resend status = Verified
- ✅ DNS propagé (vérifié mxtoolbox)

---

## 🚀 PROCHAINES ÉTAPES

**Immédiat** (après validation):
1. Envoyer batch 1 (5 emails ultra-qualifiés)
2. Monitor résultats (bounce, ouvertures)
3. Update Telegram avec résultats

**Court terme** (dimanche):
1. Batches 2, 3, 4 (15+20+20 emails)
2. Relances J+1 et J+2
3. Closer ventes manuellement si besoin

**Moyen terme** (semaine prochaine):
1. Setup Stripe payment links
2. Google Analytics
3. Optimisations A/B testing

---

## 📞 SUPPORT

**Si bloqué**:
1. Screenshot erreur
2. Ping sur Telegram avec détails
3. Je debug en <15 min

---

**Temps total**: 30 min + 5-30 min propagation DNS  
**Difficulté**: ⭐⭐☆☆☆ (moyenne)  
**Status**: ✅ Migration complète prête
