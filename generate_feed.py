import json
import os

# إعدادات الملفات والروابط
json_file_path = 'products_with_slugs.json'
xml_file_path = 'feed.xml'
base_url = 'https://sherow1982.github.io/Iraq-Store/'

def create_feed():
    # التحقق من وجود ملف البيانات
    if not os.path.exists(json_file_path):
        print(f"خطأ: الملف {json_file_path} غير موجود.")
        return

    # قراءة المنتجات
    with open(json_file_path, 'r', encoding='utf-8') as f:
        products = json.load(f)

    # بداية ملف XML
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">\n'
    xml_content += '  <channel>\n'
    xml_content += '    <title>متجر العراق</title>\n'
    xml_content += f'    <link>{base_url}</link>\n'
    xml_content += '    <description>أفضل المنتجات في العراق</description>\n'

    # إضافة المنتجات
    for product in products:
        slug = product.get('slug')
        if not slug: continue
        
        xml_content += '    <item>\n'
        xml_content += f'      <g:id>{product.get("id")}</g:id>\n'
        xml_content += f'      <g:title>{product.get("title", "").replace("&", "&amp;")}</g:title>\n'
        xml_content += f'      <g:description>{product.get("description", "").replace("&", "&amp;")}</g:description>\n'
        xml_content += f'      <g:link>{base_url}products/{slug}.html</g:link>\n'
        xml_content += f'      <g:image_link>{product.get("image_link", "").replace("&", "&amp;")}</g:image_link>\n'
        xml_content += '      <g:brand>متجر العراق</g:brand>\n'
        xml_content += '      <g:condition>new</g:condition>\n'
        xml_content += '      <g:availability>in stock</g:availability>\n'
        xml_content += f'      <g:price>{product.get("price")} IQD</g:price>\n'
        if product.get("sale_price"):
            xml_content += f'      <g:sale_price>{product.get("sale_price")} IQD</g:sale_price>\n'
        xml_content += '    </item>\n'

    # نهاية الملف
    xml_content += '  </channel>\n'
    xml_content += '</rss>'

    # حفظ الملف
    with open(xml_file_path, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"تم إنشاء ملف {xml_file_path} بنجاح ويحتوي على {len(products)} منتج.")

if __name__ == "__main__":
    create_feed()