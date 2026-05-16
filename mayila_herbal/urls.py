from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from core import views
from core.sitemaps import ProductSitemap, StaticViewSitemap

# Custom admin site branding
admin.site.site_header = '🌿 Mayila Herbal Clinic — Admin'
admin.site.site_title  = 'Mayila Herbal Admin'
admin.site.index_title = 'Welcome to Mayila Herbal Dashboard'

# Sitemaps zote zimeunganishwa hapa
sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}


def robots_txt(request):
    """
    robots.txt — inawaambia Google crawlers nini wasikisomee
    na wapi wapate sitemap.
    """
    site_url = getattr(settings, 'SITE_URL', 'https://mayilaherbalclinic.com')
    content = f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/

Sitemap: {site_url}/sitemap.xml
"""
    return HttpResponse(content, content_type='text/plain')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.products_list, name='products_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('videos/', views.videos_list, name='videos_list'),
    path('tinymce/', include('tinymce.urls')),

    path('api/video/<int:pk>/view/', views.increment_video_views, name='video_view'),

    # SEO URLs
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
