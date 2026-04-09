# 🌿 Mayila Herbal Clinic — Website

Professional Django website for Mayila Herbal Clinic, Mbalizi Mbeya Tanzania.

## ✅ Features
- **100% Customizable from Admin** — every text, color, image, video
- Product showcase with image gallery & modal viewer
- Video advertisements (Upload via Uploadcare OR YouTube embed)
- WhatsApp integration on every page
- Testimonials, FAQs, Contact section
- Announcement bar
- Mobile-responsive beautiful UI
- Supabase PostgreSQL database
- Uploadcare CDN for all images & videos

---

## 🚀 Setup Instructions

### 1. Clone & Install
```bash
git clone <your-repo>
cd mayila-herbal
pip install -r requirements.txt
```

### 2. Create `.env` file (copy from `.env.example`)
```bash
cp .env.example .env
```
Fill in your credentials:

**Supabase PostgreSQL:**
- Go to https://supabase.com → Your Project → Settings → Database
- Copy the connection string details (Host, Password, etc.)
- Use Port `6543` (Transaction pooler) for best performance

**Uploadcare:**
- Go to https://uploadcare.com → Sign up free
- Dashboard → API Keys → copy Public Key & Secret Key

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Setup Initial Data
```bash
python manage.py setup_initial_data
```

### 5. Create Admin User
```bash
python manage.py createsuperuser
```

### 6. Run Server
```bash
python manage.py runserver
```

Open: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin

---

## 🎛️ Admin Panel Guide

Login at `/admin` then:

| Section | What you can change |
|---------|---------------------|
| **Site Settings** | Logo, colors, hero text, about, contact, WhatsApp, social media, footer, SEO |
| **Products** | Add/edit/delete products with images via Uploadcare |
| **Product Categories** | Manage product categories |
| **Video Advertisements** | Upload videos or paste YouTube links |
| **Testimonials** | Customer reviews with photos |
| **FAQs** | Frequently asked questions |
| **Announcements** | Top-bar announcement banners |

### Adding a Product:
1. Admin → Products → Add Product
2. Fill name, slug (auto), description, benefits, usage
3. Click the image field → Uploadcare widget opens → upload image
4. Set `is_active = True` and `is_featured = True` to show in hero slider
5. Save!

### Adding a Video:
1. Admin → Video Advertisements → Add
2. Choose type: **Upload Video** or **YouTube**
3. For Upload: click video field → upload MP4 via Uploadcare
4. For YouTube: paste the YouTube URL
5. Upload a thumbnail image
6. Save!

### Changing Colors:
1. Admin → Site Settings → Colors section
2. Change any hex color code
3. Save → entire website updates immediately!

---

## 📁 Project Structure
```
mayila_herbal/       — Django project settings & urls
core/                — Site settings, testimonials, FAQs, announcements
products/            — Product models & views
videos/              — Video advertisement models & views
templates/
  core/base.html     — Main layout (navbar, footer, WhatsApp button)
  core/home.html     — Homepage (hero, products, videos, about, contact)
  products/list.html — Products page
  products/detail.html — Product detail page
  videos/list.html   — Videos page
```

## 🌐 Deployment (Production)
```bash
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
python manage.py collectstatic
gunicorn mayila_herbal.wsgi:application
```

---
**Built with ❤️ for Mayila Herbal Clinic, Mbeya Tanzania**
