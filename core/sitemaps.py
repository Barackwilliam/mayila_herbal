from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product


class ProductSitemap(Sitemap):
    """Kila bidhaa itakuwa na URL yake mwenyewe kwenye sitemap."""
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Product.objects.filter(is_active=True).order_by('order')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class StaticViewSitemap(Sitemap):
    """Kurasa za static: Home, Products list, Videos."""
    changefreq = 'weekly'
    priority = 1.0
    protocol = 'https'

    def items(self):
        return ['home', 'products_list', 'videos_list']

    def location(self, item):
        return reverse(item)
