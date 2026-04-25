# Satellite Property Scorer - Research & Feasibility

## Data Sources Identifiés

### 1. Luxembourg Geoportail
- URL: https://www.geoportail.lu
- **3D Viewer**: "Virtual City Map" avec couches publiques
- Données cadastrales disponibles
- **Next**: Tester API access, explorer catalogue données

### 2. Data.public.lu
- URL: https://data.public.lu
- **MCP Server expérimental** pour IA conversationnelle
- Open data luxembourgeois
- **Next**: Tester serveur MCP, voir datasets propriétés

### 3. Satellite Imagery APIs (à tester)

#### Google Earth Engine
- **Pros**: Imagerie satellite haute résolution, ML intégré
- **Cons**: Gratuit pour recherche, payant commercial
- **API**: earth-engine.google.com
- **Next**: Vérifier pricing, créer compte test

#### Mapbox Satellite
- **Pros**: API simple, pricing transparent
- **Cons**: Résolution variable selon zones
- **Pricing**: ~$5/1000 requêtes (static images)
- **Next**: Tester API sur Luxembourg

#### Planet Labs
- **Pros**: Imagerie quotidienne, très haute résolution
- **Cons**: Cher ($$$), overkill pour MVP
- **Skip pour MVP**

## MVP Architecture (Version 1)

### Input
1. Zone géographique Luxembourg (commune, quartier)
2. Critères scoring :
   - Taille propriété (m²)
   - État toiture visible (texture/couleur)
   - Présence piscine/jardin
   - Isolation bâtiment (thermographie si dispo)

### Processing
1. Fetch satellite imagery (Mapbox ou Geoportail)
2. Détection objets :
   - Segmentation toiture (couleur, texture)
   - Calcul surface propriété
   - Détection features (piscine, jardin, etc.)
3. Scoring algorithm :
   - Taille propriété: 0-30 points
   - État toiture: 0-40 points
   - Features premium: 0-30 points
   - **Score total: 0-100**

### Output
- Liste propriétés scorées >70/100
- Adresse + coordonnées GPS
- Score détaillé par critère
- Contact scraping (annuaires Luxembourg)

## Budget MVP

- Mapbox API: $50 (test 10k requêtes)
- Luxembourg data access: Gratuit (open data)
- ML model (lightweight): Gratuit (open source)
- Contact scraping tools: $20-50
- **Total MVP: ~$100-150**

## Timeline MVP

- **Jour 1-2**: Setup APIs, test data access
- **Jour 3-4**: Build scorer prototype (Python script)
- **Jour 5-6**: Test sur 100 propriétés Luxembourg-Ville
- **Jour 7**: Validation résultats, scraping contacts premiers leads
- **Total: 1 semaine** pour MVP fonctionnel

## Next Actions (Immediate)

1. ✅ Research done
2. [ ] Create Mapbox account + test API
3. [ ] Explore Geoportail API docs
4. [ ] Build Python scorer prototype
5. [ ] Test on 10 properties (proof of concept)

