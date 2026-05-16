# 🌿 Mayila Herbal Clinic — Mabadiliko ya SEO

## Files Zilizobadilishwa / Kuongezwa

### 1. `products/models.py`
- Ongeza `get_absolute_url()` — URL ya kila bidhaa
- Ongeza `get_whatsapp_msg()` — WhatsApp message default
- Ongeza `get_meta_description()` — SEO description kwa kila bidhaa
- Ongeza `get_og_image_url()` — Picha ya 1200x630 kwa social sharing

### 2. `core/sitemaps.py` *(FILE MPYA)*
- `ProductSitemap` — Inaingiza kila bidhaa kwenye sitemap.xml
- `StaticViewSitemap` — Inaingiza Home, Products, Videos

### 3. `mayila_herbal/urls.py`
- Ongeza `/sitemap.xml` — Google inaisoma kujua kurasa zote
- Ongeza `/robots.txt` — Inawaambia crawlers nini cha kusoma

### 4. `mayila_herbal/settings.py`
- Ongeza `django.contrib.sitemaps` kwenye INSTALLED_APPS
- Ongeza `SITE_URL` setting — weka domain yako halisi kwenye .env

### 5. `templates/core/base.html`
- Meta tags kamili (description, keywords, robots)
- Canonical URL — inazuia duplicate content
- Open Graph tags (WhatsApp/Facebook previews)
- Twitter Card tags
- Organization JSON-LD structured data
- Favicon support

### 6. `templates/products/detail.html`
- SEO meta kwa kila bidhaa (title, description, keywords)
- Product JSON-LD structured data — Google inaona kama "bidhaa"
- BreadcrumbList JSON-LD — Home > Products > Bidhaa kwenye Google

### 7. `templates/products/list.html`
- SEO meta kwa ukurasa wa orodha
- BreadcrumbList JSON-LD

---

## Hatua Baada ya Deploy

### 1. Ongeza SITE_URL kwenye .env:
```
SITE_URL=https://www.mayila-herbal.co.tz
```
*(Badilisha na domain halisi ya mteja)*

### 2. Submit Sitemap kwa Google Search Console:
1. Nenda https://search.google.com/search-console
2. Add Property → URL kamili ya website
3. Sitemaps → Ingiza: `sitemap.xml` → Submit
4. Google itaanza kuona kurasa zote ndani ya siku 1-7

### 3. Thibitisha robots.txt inafanya kazi:
Tembelea: `https://yourdomain.com/robots.txt`

### 4. Thibitisha sitemap:
Tembelea: `https://yourdomain.com/sitemap.xml`

---

## Matokeo Yanayotarajiwa

Baada ya Google kuindeksi:
- Kila bidhaa itatokea Google kwa jina lake
- Ukurasa wa bidhaa utaonyesha maelezo mazuri kwenye Google results
- WhatsApp/Facebook share itaonyesha picha na maelezo ya bidhaa
- "Mdindadinda Mbeya", "tiba za asili Tanzania" n.k. zitaweza kutokea Google
