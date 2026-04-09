from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductCategory
from .forms import ProductForm, ProductCategoryForm


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    form = ProductCategoryForm
    list_display = ('name', 'slug', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('product_thumb', 'name', 'category', 'volume', 'badge', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order', 'badge')
    list_filter = ('is_active', 'is_featured', 'badge', 'category')
    search_fields = ('name', 'short_desc', 'description')
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        ('📦 Basic Info', {
            'fields': ('name', 'slug', 'category', 'volume', 'targets', 'badge'),
        }),
        ('🖼️ Images (via Uploadcare)', {
            'fields': ('main_image', 'image2', 'image3', 'image4'),
            'description': 'Pakia picha moja moja — zitahifadhiwa kwenye Uploadcare CDN.',
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

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['main_image', 'image2', 'image3', 'image4']:
            # Ongeza widget attributes
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '4c3ba9de492e0e0eaddc',  # Public key iliyofaulu
                'data-images-only': 'true',
                'data-clearable': 'true',
                'data-preview-step': 'true',
                'style': 'width: 100%; padding: 10px; border: 2px dashed #ccc; border-radius: 5px;',
            })
            # Hakikisha widget ni TextInput
            from django.forms import TextInput
            formfield.widget = TextInput(attrs=formfield.widget.attrs)
        return formfield

    def product_thumb(self, obj):
        url = obj.get_thumb_url()
        if url:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:8px;">',
                url
            )
        return '—'
    product_thumb.short_description = 'Picha'