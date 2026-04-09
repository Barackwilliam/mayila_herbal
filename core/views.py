from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db import models as db_models
from .models import SiteSettings, Testimonial, FAQ
from products.models import Product, ProductCategory
from videos.models import VideoAd


def home(request):
    site = SiteSettings.get()
    featured_products = Product.objects.filter(is_active=True, is_featured=True).order_by('order')[:6]
    all_products = Product.objects.filter(is_active=True).order_by('order')
    categories = ProductCategory.objects.filter(is_active=True)
    videos = VideoAd.objects.filter(is_active=True).order_by('order')
    testimonials = Testimonial.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(is_active=True)

    return render(request, 'core/home.html', {
        'site': site,
        'featured_products': featured_products,
        'all_products': all_products,
        'categories': categories,
        'videos': videos,
        'testimonials': testimonials,
        'faqs': faqs,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(is_active=True).exclude(pk=product.pk).order_by('?')[:4]
    site = SiteSettings.get()
    return render(request, 'products/detail.html', {
        'product': product,
        'related': related,
        'site': site,
    })


def products_list(request):
    site = SiteSettings.get()
    category_slug = request.GET.get('category')
    categories = ProductCategory.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True).order_by('order')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    return render(request, 'products/list.html', {
        'products': products,
        'categories': categories,
        'site': site,
        'active_category': category_slug,
    })


def videos_list(request):
    site = SiteSettings.get()
    videos = VideoAd.objects.filter(is_active=True).order_by('order')
    return render(request, 'videos/list.html', {'videos': videos, 'site': site})


@require_POST
def increment_video_views(request, pk):
    VideoAd.objects.filter(pk=pk).update(views=db_models.F('views') + 1)
    return JsonResponse({'ok': True})
