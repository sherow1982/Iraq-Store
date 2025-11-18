#!/bin/bash

# Script to fix all product image paths by removing '../' prefix
# Run this in Git Bash or WSL in the repository root

echo "🔧 Fixing all product image paths..."

# Find all HTML files in products folder and fix image paths
find products -name "*.html" -type f -exec sed -i 's|src="../https://|src="https://|g' {} +

echo "✅ Done! All image paths fixed."
echo "📊 Files modified:"
find products -name "*.html" -type f | wc -l

echo ""
echo "🚀 Now commit and push:"
echo "   git add products/"
echo "   git commit -m 'Fix all product image paths'"
echo "   git push origin main"