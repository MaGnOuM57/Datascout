# 🚀 Guide de Déploiement Rapide - DataScout Pro

## Option 1 : Vercel (Recommandé - 2 min)

### Étapes :
1. **Créer compte Vercel** : https://vercel.com/signup
2. **Installer CLI** (optionnel) :
   ```bash
   npm install -g vercel
   ```
3. **Déployer** :
   ```bash
   cd ~/.openclaw/workspace/datascout-pro
   vercel
   ```
4. Suivre les prompts (project name: datascout-pro)
5. **URL live en 30 secondes** : `https://datascout-pro.vercel.app`

### Sans CLI (via interface web) :
1. Aller sur https://vercel.com/new
2. Uploader le dossier `datascout-pro/`
3. Cliquer "Deploy"
4. URL live : `https://datascout-pro-[random].vercel.app`

---

## Option 2 : Netlify (Alternative - 2 min)

### Via Drag & Drop :
1. Aller sur https://app.netlify.com/drop
2. Glisser-déposer le dossier `datascout-pro/`
3. URL live : `https://[random].netlify.app`

### Via CLI :
```bash
npm install -g netlify-cli
cd ~/.openclaw/workspace/datascout-pro
netlify deploy --prod
```

---

## Option 3 : GitHub Pages (Gratuit - 5 min)

### Étapes :
1. **Créer repo GitHub** : https://github.com/new
   - Nom: `datascout-pro`
   - Public
2. **Pusher le code** :
   ```bash
   cd ~/.openclaw/workspace/datascout-pro
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/[username]/datascout-pro.git
   git push -u origin main
   ```
3. **Activer GitHub Pages** :
   - Settings → Pages
   - Source: `main` branch, `/ (root)`
   - Save
4. **URL live** : `https://[username].github.io/datascout-pro/`

---

## Option 4 : Hébergement Custom

### Upload via FTP/SFTP :
- Uploader le contenu de `datascout-pro/` vers `/public_html/`
- Configurer domaine (optionnel)

---

## 🔧 Configuration Stripe (OBLIGATOIRE)

### Étape 1 : Créer compte Stripe
1. Aller sur https://dashboard.stripe.com/register
2. Compléter inscription (besoin infos entreprise)
3. Activer mode "Live" (vs Test)

### Étape 2 : Créer Payment Link
1. Dashboard → Products → Add Product
   - Name: "100 Restaurants Premium Bio/Local France"
   - Price: 149 EUR (one-time)
   - Description: "Base de données qualifiée..."
2. Cliquer "Create payment link"
3. **Copier le lien** : `https://buy.stripe.com/XXXXXXXXX`

### Étape 3 : Intégrer dans landing page
Remplacer dans `index.html` :
```html
<!-- Remplacer -->
href="https://buy.stripe.com/test_PLACEHOLDER"

<!-- Par votre vrai lien -->
href="https://buy.stripe.com/XXXXXXXXX"
```

### Étape 4 : Configurer webhook (optionnel - automatisation)
Pour livraison automatique du produit après paiement :
1. Dashboard → Developers → Webhooks
2. Add endpoint: `https://[votre-domaine]/webhook`
3. Écouter événement: `checkout.session.completed`
4. Créer script serveur qui envoie email avec fichiers

**Note** : Pour MVP, livraison manuelle = OK (email manuel après notif Stripe)

---

## 📧 Configuration Email Transactionnel (Livraison Produit)

### Option 1 : Manuel (MVP)
1. Recevoir notif Stripe (email)
2. Envoyer manuellement fichiers par email :
   - `restaurants-100-complete.csv`
   - `EXEMPLE-RAPPORT-FINAL.pdf` (convertir .md en PDF)

### Option 2 : Automatique (Scale)
**Services gratuits pour démarrer** :
- SendGrid (100 emails/jour gratuit)
- Mailgun (5,000 emails/mois gratuit)
- AWS SES (62,000 emails/mois gratuit première année)

**Script simple** (Node.js + SendGrid) :
```javascript
// webhook-handler.js
const stripe = require('stripe')(process.env.STRIPE_SECRET);
const sgMail = require('@sendgrid/mail');

app.post('/webhook', async (req, res) => {
  const event = req.body;
  
  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    const customerEmail = session.customer_email;
    
    // Envoyer email avec produit
    await sgMail.send({
      to: customerEmail,
      from: 'livraison@datascout.pro',
      subject: '🎯 Votre base de données 100 Restaurants',
      html: 'Merci pour votre achat ! Voici vos fichiers...',
      attachments: [
        { filename: 'restaurants-100.xlsx', content: '...' },
        { filename: 'guide-utilisation.pdf', content: '...' }
      ]
    });
  }
  
  res.json({received: true});
});
```

---

## ✅ Checklist Pré-Lancement

- [ ] Landing page déployée (URL fonctionnelle)
- [ ] Stripe payment link configuré (mode Live)
- [ ] Stripe link intégré dans landing page
- [ ] Email de livraison préparé (template)
- [ ] Fichiers produits prêts :
  - [ ] `restaurants-100-complete.xlsx` (Excel converti depuis CSV)
  - [ ] `Guide-Utilisation.pdf` (PDF depuis EXEMPLE-RAPPORT-FINAL.md)
- [ ] Testéun achat end-to-end (mode Test Stripe)
- [ ] Domaine personnalisé configuré (optionnel mais pro)

---

## 🌐 Domaine Personnalisé (Optionnel - 12€/an)

**Recommandation** : `datascout.pro` ou `datascout-pro.com`

### Acheter domaine :
- Namecheap : ~10€/an
- OVH : ~8€/an
- Google Domains : ~12€/an

### Configurer DNS :
**Pour Vercel** :
1. Vercel Dashboard → Domains
2. Add domain: `datascout.pro`
3. Copier records DNS (A / CNAME)
4. Ajouter dans votre registrar DNS

**Pour Netlify** :
1. Netlify Dashboard → Domain settings
2. Add custom domain: `datascout.pro`
3. Configurer CNAME : `[random].netlify.app`

---

## 📊 Analytics (Optionnel - tracking conversions)

### Google Analytics 4 (Gratuit)
1. Créer propriété : https://analytics.google.com
2. Copier Measurement ID : `G-XXXXXXXXXX`
3. Ajouter dans `<head>` de index.html :
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Plausible Analytics (Privacy-friendly, 9€/mois)
Alternative RGPD-friendly sans cookies :
```html
<script defer data-domain="datascout.pro" src="https://plausible.io/js/script.js"></script>
```

---

## 🚀 Statut Actuel

| Étape | Statut |
|-------|--------|
| Landing page HTML | ✅ Prête |
| Base 100 restaurants | ✅ Complète |
| Rapport exemple PDF | ✅ Markdown prêt |
| Stripe account | ⏳ À créer |
| Payment link | ⏳ À configurer |
| Déploiement | ⏳ Choisir option |
| Domaine | ⏳ Optionnel |

**Temps estimé pour aller live** : 15-30 minutes

---

## 💡 Recommandation CEO

**Pour MVP aujourd'hui** :
1. ✅ Vercel deploy (2 min)
2. ✅ Stripe account + payment link (10 min)
3. ✅ Convertir .md en PDF (3 min)
4. ✅ Tester achat (5 min)
5. ✅ Commencer outreach prospects (30 min)

**Total** : ~50 minutes pour être 100% opérationnel

**Domaine personnalisé** = peut attendre première vente (validation).
