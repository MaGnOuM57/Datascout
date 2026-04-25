#!/bin/bash

# Rebranding Script: DataScout Pro → Ellie VAI
# Domain: datascout.pro → ellievai.com

echo "🔄 REBRANDING EN COURS..."

cd /home/openclaw/.openclaw/workspace/datascout-pro

# Backup avant modifications
echo "📦 Création backup..."
mkdir -p backup-before-rebrand
cp index.html backup-before-rebrand/
cp vege.html backup-before-rebrand/
cp boutiques.html backup-before-rebrand/
cp caves.html backup-before-rebrand/

# Replace DataScout Pro → Ellie VAI
echo "✏️ DataScout Pro → Ellie VAI..."
sed -i 's/DataScout Pro/Ellie VAI/g' index.html vege.html boutiques.html caves.html

# Replace datascout-pro.vercel.app → ellievai.com
echo "🌐 URLs Vercel → ellievai.com..."
sed -i 's/datascout-pro\.vercel\.app/ellievai.com/g' index.html vege.html boutiques.html caves.html

# Replace emails
echo "📧 Emails datascout.pro → ellievai.com..."
sed -i 's/contact@datascout\.pro/contact@ellievai.com/g' index.html vege.html boutiques.html caves.html

# Replace domain references
echo "🔗 Domaines..."
sed -i 's/datascout\.pro/ellievai.com/g' index.html vege.html boutiques.html caves.html

# Meta tags & titles
echo "🏷️ Meta tags..."
sed -i 's/<title>DataScout Pro/<title>Ellie VAI/g' index.html vege.html boutiques.html caves.html

# Prospection emails
if [ -d "prospection" ]; then
    echo "📬 Emails prospection..."
    find prospection -type f -name "*.json" -exec sed -i 's/DataScout Pro/Ellie VAI/g' {} \;
    find prospection -type f -name "*.json" -exec sed -i 's/contact@datascout\.pro/contact@ellievai.com/g' {} \;
    find prospection -type f -name "*.json" -exec sed -i 's/datascout-pro\.vercel\.app/ellievai.com/g' {} \;
    find prospection -type f -name "*.md" -exec sed -i 's/datascout\.pro/ellievai.com/g' {} \;
fi

# Python scripts
echo "🐍 Scripts Python..."
if [ -f "prospection/send-batch-safe.py" ]; then
    sed -i 's/contact@datascout\.pro/contact@ellievai.com/g' prospection/send-batch-safe.py
    sed -i 's/DataScout Pro/Ellie VAI/g' prospection/send-batch-safe.py
fi

echo ""
echo "✅ REBRANDING TERMINÉ"
echo ""
echo "📊 Changements:"
echo "   - Marque: DataScout Pro → Ellie VAI"
echo "   - Email: contact@datascout.pro → contact@ellievai.com"
echo "   - Domaine: datascout.pro → ellievai.com"
echo "   - URLs: datascout-pro.vercel.app → ellievai.com"
echo ""
echo "💾 Backup créé dans: backup-before-rebrand/"
echo ""
echo "🚀 Prochaines étapes:"
echo "   1. Vérifie visuellement index.html"
echo "   2. git add -A && git commit -m '🎨 Rebrand → Ellie VAI'"
echo "   3. git push origin master"
echo "   4. Deploy Vercel automatique"
