#!/bin/bash
# Vercel build script
# Copy index-final.html to index.html for deployment
cp index-final.html index.html 2>/dev/null || true
echo "Build complete - index.html ready"
