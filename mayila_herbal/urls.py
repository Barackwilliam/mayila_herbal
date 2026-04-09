from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

# Custom admin site branding
admin.site.site_header = '🌿 Mayila Herbal Clinic — Admin'
admin.site.site_title  = 'Mayila Herbal Admin'
admin.site.index_title = 'Welcome to Mayila Herbal Dashboard'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.products_list, name='products_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('videos/', views.videos_list, name='videos_list'),
    path('api/video/<int:pk>/view/', views.increment_video_views, name='video_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
