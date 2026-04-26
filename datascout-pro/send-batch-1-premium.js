#!/usr/bin/env node

/**
 * DataScout Pro - Batch 1 Premium Prospects
 * Envoi automatisé cold emails ultra-personnalisés
 * Date: 2026-04-26 14:00
 */

const fs = require('fs');
const path = require('path');

// Prospects premium avec emails personnalisés
const prospects = [
  {
    email: 'direction@kaviarhouse.fr',
    company: 'Kaviar House',
    firstName: 'Madame, Monsieur',
    subject: 'Votre caviar Prunier sur 50 tables Michelin cette saison ?',
    emailBody: `Bonjour,

J'ai remarqué que Kaviar House fournit déjà certains des plus beaux restaurants de Paris – Le Bristol, Le Meurice, Plaza Athénée.

**Question directe** : combien de nouvelles tables étoilées avez-vous ouvert ces 6 derniers mois ?

J'ai une base de **100 restaurants gastronomiques** (1-3 étoiles Michelin, Gault&Millau 16+) actuellement **en recherche active de fournisseurs caviar premium** :

→ **50 restaurants 1-2 étoiles** (budget 3-8K€/mois produits fins)  
→ **25 tables bistronomiques haut de gamme** (budget 1-3K€/mois)  
→ **15 palaces/hôtels 5 étoiles** (budget 10-20K€/mois)

**Contacts directs** : Chefs, directeurs achats, F&B managers.  
**Géo** : Paris, Lyon, Côte d'Azur, Bordeaux, Strasbourg.  
**Timing** : Recherche fournisseurs printemps/été 2026.

**Votre opportunité** :  
Si votre capacité production caviar Prunier, Sturia ou Kaviar peut absorber 20-30 nouvelles tables premium cette année, cette liste vous fait gagner 6 mois de prospection.

**Livrable** : Fichier Excel complet (noms restaurants, chefs, contacts directs, emails, téléphones, budget estimé, spécialités carte).

**Prix** : 149€ (investissement récupéré sur 1 seule commande).

Intéressé pour voir 10 exemples de la liste ?

Cordialement,  
**DataScout Pro**  
Génération leads B2B restauration premium

P.S. : Cette base est mise à jour en temps réel. Les 10 premiers fournisseurs qui l'achètent ont un avantage concurrentiel sur les autres.`
  },
  {
    email: 'commercial@lazzaretti.fr',
    company: 'Lazzaretti Rungis',
    firstName: 'Madame, Monsieur',
    subject: '80 chefs cherchent le primeur des étoilés (est-ce vous ?)',
    emailBody: `Bonjour,

Lazzaretti approvisionne déjà certains des plus grands chefs de Paris depuis Rungis.

**Mais voici ma question** : combien de nouvelles tables gastronomiques avez-vous signées ces 3 derniers mois ?

Si vous cherchez à développer votre clientèle chefs étoilés et bistronomie haut de gamme, j'ai quelque chose pour vous :

**100 restaurants qualifiés** actuellement en recherche de primeur/fournisseur fruits & légumes ultra-frais :

→ **35 restaurants 1-2 étoiles Michelin** (commandes quotidiennes 500-2000€)  
→ **45 bistronomiques Gault&Millau 14-16** (3-5 livraisons/semaine)  
→ **20 tables fusion/végétales** (forte demande légumes anciens, fleurs, micro-pousses)

**Profils** : Chefs passionnés produit, recherche fournisseurs Rungis de confiance, besoin traçabilité et fraîcheur extrême.

**Géolocalisation** : Île-de-France (70%), régions (30%).

**Ce que vous recevez** :  
→ Nom restaurant + chef  
→ Email + téléphone direct  
→ Spécialités (végétal, poisson, viande, fusion...)  
→ Fréquence commandes estimée  
→ Budget mensuel fruits & légumes

**ROI** : Si vous signez 5 nouvelles tables à 3000€/mois, vous générez 180K€/an. Cette liste coûte 149€.

Voulez-vous voir 10 exemples concrets ?

Bien à vous,  
**DataScout Pro**  
Intelligence commerciale restauration B2B`
  },
  {
    email: 'pro@fossier.fr',
    company: 'Maison Fossier',
    firstName: 'Madame, Monsieur',
    subject: '100 pâtisseries innovantes attendent vos Biscuits Roses',
    emailBody: `Bonjour,

Les Biscuits Roses de Reims sont une institution depuis 1756 – mais combien de pâtisseries et restaurants desserts utilisent vos produits comme signature ?

**L'opportunité** : J'ai identifié **100 établissements** (pâtisseries, salons de thé, restaurants desserts signature) qui cherchent actuellement des **produits iconiques** pour différencier leur offre :

→ **40 pâtisseries artisanales modernes** (desserts fusion, réinterprétations classiques)  
→ **35 restaurants bistronomiques** (desserts signature, besoin biscuits haut de gamme)  
→ **25 salons de thé / coffee shops premium** (desserts à l'assiette, pâtisserie fine)

**Profil idéal pour Fossier** :  
- Chefs pâtissiers créatifs (cherchent base biscuit noble)  
- Restaurants sans pâtissier (desserts prêts-à-dresser)  
- Concept "french heritage" (Biscuits Roses = histoire + qualité)

**Ce que contient la base** :  
→ Nom établissement + chef/propriétaire  
→ Contact direct (email + téléphone)  
→ Type desserts carte (moderne, classique, fusion...)  
→ Budget estimé produits secs/biscuiterie  
→ Angle commercial suggéré

**Votre ROI** :  
Si 10 pâtisseries commandent 500€/mois, c'est 60K€/an de CA incrémental.  
Investissement : 149€.

Intéressé pour découvrir 10 profils de la liste ?

Cordialement,  
**DataScout Pro**  
Leads qualifiés restauration & pâtisserie`
  },
  {
    email: 'dev.commercial@transgourmet.fr',
    company: 'Transgourmet',
    firstName: 'Madame, Monsieur',
    subject: '100 restaurants indépendants cherchent alternative aux grossistes classiques',
    emailBody: `Bonjour,

Transgourmet est leader de la distribution CHR en France – mais voici une question intéressante :

**Combien de restaurants indépendants haut de gamme perdez-vous chaque année au profit de fournisseurs spécialisés (Rungis, circuits courts, producteurs directs) ?**

J'ai une hypothèse : ces restaurants vous échappent parce qu'ils ne savent pas que Transgourmet peut livrer la même qualité que leurs petits fournisseurs, avec la logistique d'un grand groupe.

**Ma base** : 100 restaurants indépendants premium (bistronomie, néo-bistrot, gastronomie moderne) qui cherchent actuellement **un grossiste de confiance** capable de :

→ Livrer produits frais ultra-qualité (marée J+1, viandes maturées, légumes primeur)  
→ Flexibilité commandes (petites quantités, références variées)  
→ Accompagnement commercial (pas juste drop & go)

**Profils** :  
- Chefs 30-45 ans, indépendants ou petites chaînes (2-3 restos)  
- Budget achats 15-40K€/mois  
- Actuellement multi-fournisseurs (veulent simplifier)  
- Sensibles qualité + service + prix

**Votre opportunité** :  
Si vous convertissez 20 de ces restaurants à 25K€/mois moyen, c'est 6M€ de CA annuel.

Liste complète : 149€.

Voulez-vous voir 10 profils détaillés ?

Bien cordialement,  
**DataScout Pro**  
Génération leads B2B foodservice`
  },
  {
    email: 'france.pro@electrolux.com',
    company: 'Electrolux Professional',
    firstName: 'Madame, Monsieur',
    subject: '50 ouvertures restaurants 2026 : votre part du gâteau ?',
    emailBody: `Bonjour,

Electrolux Professional équipe déjà les plus grandes cuisines professionnelles – mais voici la vraie question :

**Combien de nouvelles ouvertures restaurants ratez-vous chaque année parce que vous n'êtes pas là au bon moment (phase travaux, choix équipementier) ?**

**Ma proposition** : Je vous donne accès à **100 restaurants** en phase :
- Ouverture confirmée 2026 (50 projets)  
- Rénovation/agrandissement cuisine (30 projets)  
- Changement équipement (20 projets, fin de vie matériel)

**Segments** :  
→ **Bistronomie moderne** (cuisine ouverte, design, équipement visible)  
→ **Restaurants gastronomiques** (équipement haut de gamme, fiabilité pro)  
→ **Concepts multi-sites** (chaînes 3-10 restos, standardisation équipement)

**Ce que vous recevez** :  
→ Nom projet + porteur  
→ Contact décideur (chef, gérant, architecte, maître d'œuvre)  
→ Phase projet (études, travaux, équipement)  
→ Budget équipement estimé  
→ Date ouverture prévue

**Votre ROI** :  
1 cuisine complète = 40-80K€.  
Si vous équipez 10 cuisines sur les 100, c'est 400-800K€ de CA.  
Investissement liste : 149€.

Intéressé pour voir 10 projets détaillés ?

Cordialement,  
**DataScout Pro**  
Intelligence commerciale CHR & projets restauration`
  }
];

// Mode DRY RUN - Génération des commandes curl
console.log('🚀 DataScout Pro - Batch 1 Premium (DRY RUN)');
console.log('📅 Date:', new Date().toISOString());
console.log('🎯 Prospects:', prospects.length);
console.log('');

// Lecture du token Resend
const envPath = path.join(__dirname, '.env');
let resendKey = '';

try {
  const envContent = fs.readFileSync(envPath, 'utf8');
  const match = envContent.match(/RESEND_API_KEY=(.+)/);
  if (match) {
    resendKey = match[1].trim();
  }
} catch (err) {
  console.error('❌ Erreur lecture .env:', err.message);
  process.exit(1);
}

if (!resendKey || resendKey === 'your_resend_api_key_here') {
  console.error('❌ RESEND_API_KEY manquant ou invalide dans .env');
  process.exit(1);
}

console.log('✅ RESEND_API_KEY trouvé');
console.log('');

// Génération des commandes curl (mode DRY RUN)
console.log('📧 COMMANDES CURL À EXÉCUTER:\n');

prospects.forEach((prospect, index) => {
  const payload = {
    from: 'DataScout Pro <contact@datascout.pro>',
    to: [prospect.email],
    subject: prospect.subject,
    text: prospect.emailBody,
    tags: [
      { name: 'campaign', value: 'batch-1-premium' },
      { name: 'company', value: prospect.company },
      { name: 'date', value: '2026-04-26' }
    ]
  };

  const curlCommand = `curl -X POST 'https://api.resend.com/emails' \\
  -H 'Authorization: Bearer ${resendKey}' \\
  -H 'Content-Type: application/json' \\
  -d '${JSON.stringify(payload).replace(/'/g, "\\'")}'`;

  console.log(`# Email ${index + 1}/${prospects.length} - ${prospect.company}`);
  console.log(curlCommand);
  console.log('');
});

console.log('\n📊 SUMMARY:');
console.log(`Total emails: ${prospects.length}`);
console.log(`Mode: DRY RUN (review only)`);
console.log('');
console.log('⚠️  Pour envoyer réellement les emails:');
console.log('1. Review les commandes ci-dessus');
console.log('2. Exécute chaque curl manuellement');
console.log('3. OU modifie ce script pour POST direct via fetch/axios');
console.log('');
console.log('💡 Prochaine étape: Créer send-batch-1-premium-LIVE.js avec envoi réel');
