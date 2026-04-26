#!/usr/bin/env node

/**
 * Scraper Artisans BTP Luxembourg
 * 
 * Sources:
 * 1. editus.lu (Pages Jaunes Luxembourg)
 * 2. Google Maps
 * 3. LinkedIn
 * 
 * Target: 50-100 artisans (plombiers, électriciens, maçons)
 */

const https = require('https');
const fs = require('fs');

// Categories to scrape
const CATEGORIES = [
  { name: 'Plombiers', query: 'plombier' },
  { name: 'Électriciens', query: 'électricien' },
  { name: 'Maçons', query: 'maçon' },
  { name: 'Chauffagistes', query: 'chauffagiste' },
  { name: 'Peintres', query: 'peintre' },
  { name: 'Menuisiers', query: 'menuisier' }
];

const LOCATIONS = [
  'Luxembourg',
  'Esch-sur-Alzette',
  'Differdange',
  'Dudelange',
  'Ettelbruck'
];

// Manual research URLs (to be used in browser)
console.log('🔍 SOURCES DE RECHERCHE ARTISANS BTP LUXEMBOURG\n');

CATEGORIES.forEach(cat => {
  console.log(`\n📋 ${cat.name}:`);
  console.log(`   Editus: https://www.editus.lu/fr/recherche?what=${cat.query}&where=luxembourg`);
  console.log(`   Google: https://www.google.com/maps/search/${cat.query}+luxembourg`);
  console.log(`   LinkedIn: https://www.linkedin.com/search/results/people/?keywords=${cat.query}%20luxembourg`);
});

console.log('\n\n📊 STRUCTURE CSV OUTPUT:\n');
console.log('Nom,Entreprise,Téléphone,Email,Site,Adresse,Ville,Spécialité,Source\n');

console.log('💡 NEXT STEPS:');
console.log('1. Open browser and visit URLs above');
console.log('2. Copy contacts to artisans-luxembourg.csv');
console.log('3. Run validation script');
console.log('4. Prepare LinkedIn messages');
console.log('5. Start phone calls\n');

// Create output CSV if doesn't exist
const csvPath = './artisans-luxembourg.csv';
if (!fs.existsSync(csvPath)) {
  fs.writeFileSync(csvPath, 'Nom,Entreprise,Téléphone,Email,Site,Adresse,Ville,Spécialité,Source,Intérêt,Notes\n');
  console.log(`✅ Created ${csvPath}`);
}

console.log('\n🎯 TARGET: 50 artisans today');
console.log('⏰ DEADLINE: 12h (2 hours)\n');
