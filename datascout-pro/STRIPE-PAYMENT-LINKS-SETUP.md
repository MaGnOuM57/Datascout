# 🔗 STRIPE PAYMENT LINKS - Setup 5 Minutes

**Objectif**: Créer 4 payment links pour les 4 produits (remplacer liens demo actuels sur site)

---

## 📋 PRÉPARATION (Copier-coller direct)

### Produit 1: Restaurants Bio Pro (Featured)
```
Nom: 100 Restaurants Premium France - Leads Bio/Local
Prix: 149 EUR
Description: Liste qualifiée de 100 restaurants bio/locavores France avec contacts décideurs, scoring IA, scripts de vente. Livraison immédiate par email.
```

### Produit 2: Restaurants Végétariens/Vegan
```
Nom: 50 Restaurants Végétariens/Vegan Premium France
Prix: 99 EUR
Description: Base exclusive de 50 restaurants 100% végé/vegan en France. Aucune base B2B végé n'existe ailleurs. Contacts décideurs + scoring IA.
```

### Produit 3: Boutiques Bio
```
Nom: 30 Boutiques Bio Majeures - Contacts Achats
Prix: 79 EUR
Description: Accès responsables achats de 30 enseignes bio majeures (Biocoop, Naturalia, La Vie Claire, etc.). Mix chaînes nationales + indépendants.
```

### Produit 4: Caves à Vin Premium
```
Nom: 30 Caves à Vin Premium + Bars à Vins
Prix: 79 EUR
Description: 30 caves premium (60% focus vins naturels/bio). Caves historiques (Cave Augé 1850, Legrand 1880) + modernes. Contacts décideurs.
```

---

## 🚀 CRÉATION (Stripe Dashboard - 5 min)

### Étape 1: Créer les produits
1. Va sur **https://dashboard.stripe.com/products** (mode PRODUCTION)
2. Clique **"+ Add product"**
3. Pour chaque produit (répéter 4x):
   - **Name**: (copier nom ci-dessus)
   - **Description**: (copier description ci-dessus)
   - **Pricing**:
     - Type: **One-time**
     - Price: **EUR** (montant ci-dessus)
   - **Tax**: Pas de taxe pour l'instant (ou ajouter TVA si nécessaire)
   - Clique **"Save product"**

### Étape 2: Créer les Payment Links
Pour chaque produit (4x):
1. Clique sur le produit dans la liste
2. Clique **"Create payment link"**
3. Configuration:
   - **Quantity**: 1 (fixed)
   - **After payment**: Redirect to URL → `https://ellievai.com/merci.html` (page à créer)
   - **Collect customer info**: Email (requis pour livraison)
   - **Allow promotion codes**: Oui (pour futures promos)
4. Clique **"Create link"**
5. **Copie le lien généré** (ex: `https://buy.stripe.com/...`)

---

## 📝 LIENS À REMPLACER (sur site)

Une fois les 4 liens créés, m'envoyer les 4 URLs comme ça:

```
PRO: https://buy.stripe.com/...
VEGE: https://buy.stripe.com/...
BOUTIQUES: https://buy.stripe.com/...
CAVES: https://buy.stripe.com/...
```

Je les update automatiquement sur le site (index.html, vege.html, boutiques.html, caves.html).

---

## ✨ PAGE MERCI (Bonus - Optionnel)

Créer `merci.html` pour post-achat:

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Merci pour votre achat! - Ellie VAI</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      max-width: 600px;
      margin: 100px auto;
      padding: 40px;
      text-align: center;
    }
    h1 { color: #8B5CF6; }
    .icon { font-size: 80px; margin-bottom: 20px; }
  </style>
</head>
<body>
  <div class="icon">✅</div>
  <h1>Paiement confirmé!</h1>
  <p>Votre liste sera dans votre boîte mail dans <strong>2-5 minutes</strong>.</p>
  <p>Vérifiez vos spams si vous ne voyez rien.</p>
  <p><a href="https://ellievai.com">← Retour au site</a></p>
</body>
</html>
```

Je peux créer cette page maintenant si tu veux (ou après).

---

## 🎯 PRIORITÉ

**Urgent**: Produit 1 (Pro 149€) - C'est celui sur lequel on va avoir le plus de conversions

**Peut attendre**: Produits 2-4 (on a moins de trafic dessus pour l'instant)

---

**ETA total**: 5 min si tu fais juste Produit 1, 15 min si tu fais les 4.

Une fois créé, envoie-moi les liens et je les intègre sur le site en 2 min.
