#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سكريبت لإنشاء جميع صفحات المنتجات (640 صفحة) مع تحسينات SEO كاملة
استخدام: python generate_products.py
"""

import json
import os
from urllib.parse import quote

print("="*70)
print("🚀 سكريبت إنشاء صفحات المنتجات المحسّن")
print("="*70)

# تحميل المنتجات
print("\n📂 جاري تحميل بيانات المنتجات...")
with open('products_final.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print(f"✅ تم تحميل {len(products)} منتج")

# إنشاء مجلد products
os.makedirs('products', exist_ok=True)

# دالة لإنشاء صفحة منتج واحدة
def create_product_page(product):
    whatsapp_number = "201110760081"
    discount = round(((product['price'] - product['sale_price']) / product['price']) * 100) if product.get('price') and product.get('sale_price') else 0

    # رسالة WhatsApp
    title = product.get('title', 'منتج')
    sale_price = product.get('sale_price', 0)
    whatsapp_message = f"مرحباً، أريد طلب المنتج التالي:%0A%0A📦 {quote(title)}%0A💰 السعر: {sale_price:,} د.ع"
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"

    # مسار الصورة الصحيح (بدون ../)
    image_url = product.get('image_link', '')

    # الوصف
    description = product.get('description', 'منتج عالي الجودة بأفضل سعر')[:160]

    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO Meta Tags -->
    <title>{title} - متجر العراق</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{title}, متجر العراق, {title} سعر, شراء {title}">
    <meta name="author" content="متجر العراق">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://sherow1982.github.io/1/products/{product.get('slug', '')}.html">

    <!-- Open Graph -->
    <meta property="og:type" content="product">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{image_url}">
    <meta property="og:url" content="https://sherow1982.github.io/1/products/{product.get('slug', '')}.html">
    <meta property="og:price:amount" content="{sale_price}">
    <meta property="og:price:currency" content="IQD">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{image_url}">

    <!-- Bootstrap RTL -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">

    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org/",
      "@type": "Product",
      "name": "{title}",
      "image": "{image_url}",
      "description": "{description}",
      "offers": {{
        "@type": "Offer",
        "price": "{sale_price}",
        "priceCurrency": "IQD",
        "availability": "https://schema.org/InStock"
      }}
    }}
    </script>

    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Cairo', sans-serif; direction: rtl; background-color: #f8f9fa; line-height: 1.8; }}
        .navbar {{ background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); padding: 1rem 0; position: sticky; top: 0; z-index: 1000; }}
        .navbar-brand {{ font-size: 1.8rem; font-weight: bold; color: #667eea !important; text-decoration: none; }}
        .product-container {{ max-width: 1200px; margin: 2rem auto; padding: 0 1rem; }}
        .product-header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 15px 15px 0 0; }}
        .product-header h1 {{ font-size: 2rem; font-weight: 700; margin: 0; }}
        .product-content {{ background: white; border-radius: 0 0 15px 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); overflow: hidden; }}
        .product-image {{ width: 100%; max-width: 500px; height: auto; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
        .price-section {{ background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin: 1.5rem 0; }}
        .old-price {{ text-decoration: line-through; color: #999; font-size: 1.2rem; margin-left: 1rem; }}
        .new-price {{ font-size: 2.5rem; color: #667eea; font-weight: 700; }}
        .discount-badge {{ display: inline-block; background: #e74c3c; color: white; padding: 0.5rem 1rem; border-radius: 25px; font-size: 1.2rem; font-weight: 600; margin-right: 1rem; }}
        .description {{ font-size: 1.1rem; color: #555; line-height: 2; padding: 1.5rem 0; }}
        .btn-whatsapp {{ background: #25D366; color: white; border: none; padding: 1rem 3rem; font-size: 1.3rem; font-weight: 700; border-radius: 50px; cursor: pointer; transition: all 0.3s ease; text-decoration: none; display: inline-block; margin: 1rem 0; box-shadow: 0 5px 15px rgba(37, 211, 102, 0.3); }}
        .btn-whatsapp:hover {{ background: #128C7E; transform: translateY(-2px); box-shadow: 0 7px 20px rgba(37, 211, 102, 0.4); color: white; }}
        .btn-back {{ background: #667eea; color: white; border: none; padding: 0.75rem 2rem; font-size: 1rem; font-weight: 600; border-radius: 10px; text-decoration: none; display: inline-block; margin-bottom: 1rem; }}
        .btn-back:hover {{ background: #5568d3; color: white; }}
        footer {{ background: #2d3748; color: white; padding: 2rem 0; margin-top: 3rem; text-align: center; }}
        @media (max-width: 768px) {{ .product-header h1 {{ font-size: 1.5rem; }} .new-price {{ font-size: 2rem; }} .btn-whatsapp {{ padding: 0.85rem 2rem; font-size: 1.1rem; }} }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a class="navbar-brand" href="../index.html">🛒 متجر العراق</a>
        </div>
    </nav>

    <div class="product-container">
        <a href="../index.html" class="btn-back">← العودة للرئيسية</a>

        <div class="product-header">
            <h1>{title}</h1>
        </div>

        <div class="product-content">
            <div class="row p-4">
                <div class="col-md-6 text-center">
                    <img src="{image_url}" alt="{title}" class="product-image" loading="lazy">
                </div>

                <div class="col-md-6">
                    <div class="price-section">
                        <div class="mb-3">
                            <span class="discount-badge">خصم {discount}%</span>
                        </div>
                        <div>
                            <span class="old-price">{product.get('price', 0):,} د.ع</span>
                        </div>
                        <div class="new-price">{sale_price:,} د.ع</div>
                    </div>

                    <div class="description">
                        <h3 style="color: #2d3748; margin-bottom: 1rem;">📋 وصف المنتج</h3>
                        <p>{product.get('description', 'منتج عالي الجودة بأفضل سعر')}</p>
                    </div>

                    <div class="text-center mt-4">
                        <a href="{whatsapp_url}" target="_blank" rel="noopener" class="btn-whatsapp">
                            📱 اطلب المنتج واتساب
                        </a>
                        <p class="mt-3" style="color: #666; font-size: 0.95rem;">
                            سيتم فتح محادثة واتساب مع تفاصيل المنتج
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <div class="container">
            <p>© 2025 متجر العراق - جميع الحقوق محفوظة</p>
            <p style="font-size: 0.9rem; margin-top: 0.5rem; opacity: 0.7;">
                للاستفسارات: <a href="https://wa.me/201110760081" style="color: #25D366;">واتساب</a>
            </p>
        </div>
    </footer>
</body>
</html>"""

    return html

# إنشاء الصفحات
print(f"\n🔄 جاري إنشاء {len(products)} صفحة...")
print("="*70)

created_count = 0
errors = []

for i, product in enumerate(products, 1):
    try:
        page_html = create_product_page(product)
        slug = product.get('slug', f'product-{i}')
        filename = f"products/{slug}.html"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_html)

        created_count += 1

        if i % 50 == 0:
            print(f"✅ تم إنشاء {i}/{len(products)} صفحة...")

    except Exception as e:
        errors.append((product.get('id', i), str(e)))

print(f"\n{'='*70}")
print(f"✅ انتهى! تم إنشاء {created_count} صفحة بنجاح!")

if errors:
    print(f"\n⚠️ {len(errors)} خطأ:")
    for error_id, error_msg in errors[:5]:
        print(f"   - منتج {error_id}: {error_msg}")

print(f"\n{'='*70}")
print("📁 الصفحات موجودة في مجلد: products/")
print("🌐 يمكنك الآن رفع الملفات على GitHub")
print("\n✨ التحسينات المضافة:")
print("   1. ✅ إصلاح مسار الصور (بدون ../)")
print("   2. ✅ تحسينات SEO كاملة")
print("   3. ✅ Structured Data")
print("   4. ✅ Open Graph Tags")
print("   5. ✅ Twitter Cards")
print("="*70)
