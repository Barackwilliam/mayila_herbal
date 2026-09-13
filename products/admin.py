from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductCategory
from .forms import ProductAdminForm, ProductCategoryForm


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    form = ProductCategoryForm
    list_display = ('name', 'slug', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = ('main_image_thumb', 'name', 'category', 'volume', 'badge', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order', 'badge')
    list_filter = ('is_active', 'is_featured', 'badge', 'category')
    search_fields = ('name', 'short_desc', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('current_images_preview',)

    fieldsets = (
        ('📦 Basic Info', {
            'fields': ('name', 'slug', 'category', 'volume', 'targets', 'badge'),
        }),
        ('🖼️ Images (Supabase Storage)', {
            'fields': (
                'current_images_preview',
                'main_image', 'main_image_upload',
                'image2', 'image2_upload',
                'image3', 'image3_upload',
                'image4', 'image4_upload',
            ),
            'description': 'Pakia picha — zitahifadhiwa moja kwa moja kwenye Supabase Storage bucket. Acha wazi kuweka picha ile ile ya zamani.',
        }),
        ('📝 Content', {
            'fields': ('short_desc', 'description', 'benefits', 'ingredients', 'usage'),
        }),
        ('⚙️ Visibility', {
            'fields': ('is_active', 'is_featured', 'order'),
        }),
        ('💬 WhatsApp', {
            'fields': ('whatsapp_message',),
        }),
    )

    # ✅ Hii inahakikisha TinyMCE JS inapakia vizuri kwenye admin
    class Media:
        js = ('//cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js',)

    def main_image_thumb(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:8px;">',
                obj.get_image_url()
            )
        return '—'
    main_image_thumb.short_description = 'Picha'

    def current_images_preview(self, obj):
        if not obj.pk:
            return "Hifadhi bidhaa kwanza kabla ya kupakia picha."
        picha_zilizopo = obj.images
        if not picha_zilizopo:
            return "Hakuna picha bado."
        html = '<div style="display: flex; gap: 8px;">'
        for url in picha_zilizopo:
            html += f'<img src="{url}" style="max-height:80px; border-radius:6px; border:1px solid #ddd;" />'
        html += '</div>'
        return format_html(html)
    current_images_preview.short_description = "Picha za sasa"