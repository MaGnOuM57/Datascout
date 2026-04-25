# Batch 2 - Scraping Plan (35 prospects)

## 🎯 Objectif
35 prospects additionnels ultra-qualifiés (scoring 8-10/10)

---

## 🔍 Sources de données

### 1. Producteurs Bio France (15 prospects)
**Critères**:
- Producteurs maraîchers bio certifiés
- Régions: Île-de-France, Rhône-Alpes, PACA, Nouvelle-Aquitaine
- Vente directe restaurants existante (preuve de B2B mindset)
- Présence web/email pro

**Sources**:
- Annuaire Bio Partenaire
- Fédération Nationale d'Agriculture Biologique (FNAB)
- Biocoop producteurs partenaires
- Google Maps "producteur bio + ville"

**Exemple profil target**:
- Ferme du Soleil (maraîcher bio Provence, 20 ha, circuits courts)
- Email: contact@fermedusoleil.fr
- Scoring: 9/10 (déjà vend à quelques restos, cherche à développer)

---

### 2. Grossistes Bio Régionaux (10 prospects)
**Critères**:
- Grossistes fruits/légumes bio
- Distribution restaurants (pas uniquement magasins)
- CA >500k€ (équipe commerciale structurée)
- Régions: toute France

**Sources**:
- Synabio (Syndicat National des Entreprises Bio)
- Pages Jaunes "grossiste bio"
- LinkedIn "directeur commercial bio"

**Exemple profil target**:
- ProNatura Distribution (grossiste bio Sud-Ouest, 50 clients restos)
- Email: commercial@pronatura-distrib.fr
- Scoring: 8/10 (budget confirmé, cherche nouveaux débouchés)

---

### 3. Distributeurs Spécialisés (5 prospects)
**Critères**:
- Distributeurs vin bio/naturel
- Marée/poisson bio/durable
- Fromages fermiers/AOP

**Sources**:
- Annuaires vins naturels
- Réseaux fromageries artisanales
- Poissonneries bio/label MSC

**Exemple profil target**:
- Vins Vivants (caviste B2B Paris, 200 références vin naturel)
- Email: pro@vinsvivants.com
- Scoring: 9/10 (vend déjà à 50+ restaurants, cherche nouveaux clients)

---

### 4. Plateformes/Marketplaces (5 prospects)
**Critères**:
- Plateformes approvisionnement restaurants
- Tech-savvy, data-driven
- Modèle B2B SaaS ou marketplace

**Sources**:
- BPI France Deep Tech
- FoodTech startups France
- LinkedIn "founder foodtech"

**Exemple profil target**:
- FreshConnect (plateforme producteurs-restaurants, 500 users)
- Email: hello@freshconnect.io
- Scoring: 10/10 (tech mindset, comprendront value data)

---

## 📋 Données à collecter (par prospect)

1. **Nom entreprise**
2. **Contact email** (priorité: commercial@, contact@, hello@)
3. **Prénom contact** (pour personnalisation email)
4. **Ville/Région**
5. **Type activité** (maraîcher, grossiste, caviste, etc.)
6. **Taille estimée** (CA, nb employés, nb clients restos)
7. **Scoring 0-10** (probabilité achat)
8. **Raison scoring** (pourquoi 8-10/10)

---

## 🤖 Méthode scraping

**Manuel intelligent** (pas de bots):
1. Google search ciblée (ex: "producteur bio maraîcher Lyon circuits courts restaurant")
2. Vérification site web (présence section Pro/B2B = bon signe)
3. Extraction email (contact, team page, footer)
4. LinkedIn pour nom contact (ex: "commercial chez BioCoop Provence")
5. Validation email format (no-reply = skip)

**Temps estimé**: 35 prospects × 5 min = ~3h (étalement sur samedi soir + dimanche matin)

---

## 🎯 Scoring criteria (8-10/10 uniquement)

**10/10**:
- Déjà vend à restaurants (preuve de fit)
- Budget confirmé (CA >500k ou levée de fonds)
- Tech-savvy (site moderne, présence LinkedIn)
- Besoin évident (section "développement commercial" sur site)

**9/10**:
- Activité B2B structurée
- Région à fort potentiel restaurants (Paris, Lyon, Bordeaux)
- Certification bio/label qualité
- Contact direct trouvé (nom + email)

**8/10**:
- B2B probable mais pas confirmé
- Email générique (contact@) mais site pro
- Région moyenne densité restaurants
- Fit produit évident

**<8/10**: SKIP (trop incertain, pas prioritaire)

---

## 📊 Output attendu

**Fichier**: `batch-2-prospects.json`

```json
[
  {
    "company": "Ferme du Soleil",
    "email": "contact@fermedusoleil.fr",
    "first_name": "Marie",
    "city": "Avignon",
    "type": "Producteur maraîcher bio",
    "size": "20 ha, 5 employés, vend à 10 restos",
    "scoring": 9,
    "reason": "Déjà circuits courts actifs, région PACA forte densité restos bio"
  }
]
```

**Target**: 35 prospects, scoring moyen ≥8.5/10

---

## ⏱️ Planning exécution

**Samedi soir (20h-22h)**:
- Batch 2A: 15 producteurs bio (1h30)

**Dimanche matin (9h-11h)**:
- Batch 2B: 10 grossistes (1h)
- Batch 2C: 10 distributeurs/plateformes (30 min)

**Dimanche 11h**:
- Review qualité (scoring ≥8?)
- Génération emails personnalisés (30 min)
- Prêt pour envoi batch 2 (dès Resend OK)

---

**Status**: Draft, exécution démarrage immédiat  
**Owner**: Agent (autonome)  
**Validation**: Aucune requise (<300€)
