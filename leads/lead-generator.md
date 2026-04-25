# LEAD GENERATOR — ApporteurCash AI

## Système de Scoring Intelligent (0-10)

### Critères de scoring :
1. **Prix propriété** (budget potentiel)
   - <500k€ : 3/10
   - 500k-1M€ : 6/10
   - 1M-2M€ : 8/10
   - >2M€ : 10/10

2. **Surface** (volume travaux potentiel)
   - <100m² : 4/10
   - 100-200m² : 6/10
   - 200-300m² : 8/10
   - >300m² : 10/10

3. **Type de propriété**
   - Appartement : 5/10
   - Duplex : 6/10
   - Maison individuelle : 8/10
   - Multi-family house : 9/10
   - Villa/Château : 10/10

4. **Âge estimé** (via analyse photos/annonce)
   - Neuf (<5 ans) : 3/10
   - Récent (5-15 ans) : 5/10
   - Moyen (15-30 ans) : 7/10
   - Ancien (>30 ans) : 9/10

5. **Indicateurs visuels détectés**
   - Toiture vieille/dégradée : +2
   - Façade abîmée : +2
   - Jardin non entretenu : +1
   - Fenêtres anciennes : +1
   - Gouttières rouillées : +1

## Détection Automatique de Besoins

### Corps de métier ciblés :
- **Toiture** : tuiles cassées, mousse, gouttières
- **Façade** : fissures, peinture écaillée, crépi dégradé
- **Menuiserie** : fenêtres simple vitrage, portes anciennes
- **Électricité** : installation >20 ans
- **Plomberie** : tuyauterie ancienne visible
- **Isolation** : propriétés pré-2000
- **Peinture** : façade/intérieur à rafraîchir
- **Jardin/Paysagisme** : grandes propriétés non entretenues

## Format Lead Qualifié

```json
{
  "id": "LUX-2026-001",
  "score": 9.2,
  "propriete": {
    "adresse_estimee": "Luxembourg-Ville, quartier Belair",
    "prix": 1690000,
    "surface_m2": 242,
    "type": "Single-family detached house",
    "chambres": 4
  },
  "besoins_detectes": [
    {
      "corps_metier": "Toiture",
      "urgence": "haute",
      "budget_estime": "25000-35000€",
      "description": "Toiture ardoise ancienne, tuiles manquantes visibles sur photo satellite"
    },
    {
      "corps_metier": "Façade",
      "urgence": "moyenne",
      "budget_estime": "15000-20000€",
      "description": "Crépi façade sud dégradé, humidité visible"
    },
    {
      "corps_metier": "Menuiserie",
      "urgence": "moyenne",
      "budget_estime": "30000-40000€",
      "description": "Fenêtres bois simple vitrage à remplacer (12 fenêtres)"
    }
  ],
  "contact": {
    "methode": "via_agence_immobiliere",
    "timing": "propriete_en_vente_active",
    "approche": "proposition_simulation_renovation"
  },
  "valeur_lead": "80€",
  "corps_metier_principal": "Toiture",
  "probabilite_conversion": "85%"
}
```

## Workflow d'Apport de Lead

1. **Détection** : Scraping + analyse satellite
2. **Scoring** : Algorithme multi-critères
3. **Qualification** : Vérification budget + besoins réels
4. **Enrichissement** : Contact agence, photos HD, historique
5. **Packaging** : Lead complet avec simulation visuelle
6. **Vente** : 50-80€ cash par lead selon qualité

---

**Objectif immédiat** : 10 leads qualifiés score >8/10 = 500-800€ cash
