#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Performance Optimization Script for Product Pages
Optimizes LCP, CLS, and asset loading for all product HTML files
"""

import re
from pathlib import Path

def optimize_html(filepath):
    """Optimizes a product HTML file for performance."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False

        # 1. Optimize Font Loading (Non-blocking)
        if 'family=Cairo:wght@400;500;600;700;800&display=swap" rel="stylesheet">' in content:
            content = re.sub(
                r'<link href="https://fonts\.googleapis\.com/css2\?family=Cairo:wght@400;500;600;700;800&display=swap" rel="stylesheet">',
                '<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap" rel="stylesheet" media="print" onload="this.media=\'all\'">\n    <noscript><link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap" rel="stylesheet"></noscript>',
                content
            )
            modified = True

        # 2. Add preconnect to media.taager.com
        if '<link rel="preconnect" href="https://fonts.googleapis.com">' in content and 'preconnect" href="https://media.taager.com"' not in content:
            content = content.replace(
                '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
                '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n    <link rel="preconnect" href="https://media.taager.com">'
            )
            modified = True

        # 3. Optimize Main Product Image (LCP element)
        # Add fetchpriority="high" and explicit dimensions
        pattern = r'(<img src="[^"]+"\s+alt="[^"]*"\s+class="product-image[^"]*"\s+loading="eager")'
        if 'fetchpriority="high"' not in content and re.search(pattern, content):
            content = re.sub(
                pattern + r'(\s+itemprop="image")',
                r'\1 fetchpriority="high" width="360" height="360"\2',
                content
            )
            modified = True

        # 4. Add width/height to images without dimensions
        # Main product image
        content = re.sub(
            r'(<img src="[^"]+"\s+alt="[^"]*"\s+class="product-image[^"]*"\s+loading="eager"\s+itemprop="image")(\s+onerror)',
            r'\1 width="360" height="360"\2',
            content
        )
        
        # Thumbnail images
        content = re.sub(
            r'(<img src="[^"]+"\s+alt="[^"]*"\s+class="w-full h-full object-cover rounded-md)("\s+loading="lazy">)',
            r'\1" loading="lazy" width="120" height="120">',
            content
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
        
    except Exception as e:
        print(f"❌ Error in {filepath.name}: {e}")
        return False

def main():
    print("=" * 60)
    print("🚀 Product Pages Performance Optimizer")
    print("=" * 60)
    
    products_dir = Path('products')
    if not products_dir.exists():
        print("❌ Products directory not found!")
        return

    html_files = [f for f in products_dir.glob('*.html') if f.name != 'index.html']
    total = len(html_files)
    
    print(f"\n📦 Found {total} product pages to optimize\n")

    success = 0
    for i, html_file in enumerate(html_files, 1):
        if optimize_html(html_file):
            success += 1
            if i % 100 == 0:
                print(f"✅ Progress: {i}/{total} ({i*100//total}%)")

    print(f"\n{'='*60}")
    print(f"✨ Optimization Complete!")
    print(f"✅ Successfully optimized: {success}/{total} files")
    print(f"{'='*60}\n")
    
    print("📊 Applied Optimizations:")
    print("  • Non-blocking font loading")
    print("  • Preconnect to image CDN")
    print("  • fetchpriority='high' on LCP images")
    print("  • Explicit width/height on all images")
    print()

if __name__ == "__main__":
    main()
