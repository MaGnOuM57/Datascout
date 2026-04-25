# Configuration Vercel pour ellievai.com

## 🎯 Objectif

Faire pointer ellievai.com et www.ellievai.com vers ton site Vercel.

---

## 📝 Étapes

### 1. Connexion Vercel

Va sur: https://vercel.com/dashboard

**Projet actuel**: `datascout-pro`

---

### 2. Ajouter le domaine custom

1. Dans ton projet Vercel, clique **Settings** (onglet)
2. Scroll jusqu'à **Domains**
3. Clique **Add**
4. Entre: `ellievai.com`
5. Clique **Add**

Vercel va te demander de configurer DNS (déjà fait à l'étape 1 OVH).

---

### 3. Ajouter www aussi

1. Répète l'étape 2 avec: `www.ellievai.com`
2. Vercel va auto-redirect www → ellievai.com (ou inverse selon config)

---

### 4. Vérifier Vercel

Après ajout, Vercel affiche le status:
- ⏳ **Pending**: DNS pas encore propagé (attends 5-30 min)
- ✅ **Valid**: Domaine configuré correctement

---

### 5. SSL/HTTPS Automatique

Vercel génère automatiquement un certificat SSL (Let's Encrypt).

**Temps**: 1-5 min après validation domaine.

Tu verras:
- 🔒 **SSL Certificate**: Active

---

## ✅ Test après config

1. Va sur https://ellievai.com
2. Vérifie que le site s'affiche
3. Vérifie HTTPS (cadenas vert dans navigateur)
4. Test www: https://www.ellievai.com (doit rediriger vers ellievai.com)

---

## 🚨 Problèmes courants

### "Domain not configured"
- **Cause**: DNS pas encore propagé
- **Solution**: Attends 30 min, refresh

### "Invalid Configuration"
- **Cause**: Record A pointe pas vers Vercel
- **Solution**: Vérifie record A = 76.76.21.21 dans OVH

### SSL Pending
- **Cause**: Vercel génère certificat
- **Solution**: Attends 5 min max

---

## 🔄 Redirection automatique

Par défaut, Vercel redirige:
- http → https ✅
- www → sans www (ou inverse selon config)

Si tu veux changer comportement:
1. Settings → Domains
2. Clique sur domaine
3. "Redirect to" → choisis comportement

---

**Temps total**: 5 min + 5-30 min propagation DNS
