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


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     form = ProductForm
#     list_display = ('main_image', 'name', 'category', 'volume', 'badge', 'is_featured', 'is_active', 'order')
#     list_editable = ('is_featured', 'is_active', 'order', 'badge')
#     list_filter = ('is_active', 'is_featured', 'badge', 'category')
#     search_fields = ('name', 'short_desc', 'description')
#     prepopulated_fields = {'slug': ('name',)}

#     fieldsets = (
#         ('📦 Basic Info', {
#             'fields': ('name', 'slug', 'category', 'volume', 'targets', 'badge'),
#         }),
#         ('🖼️ Images (via Uploadcare)', {
#             'fields': ('main_image', 'image2', 'image3', 'image4'),
#             'description': 'Pakia picha moja moja — zitahifadhiwa kwenye Uploadcare CDN.',
#         }),
#         ('📝 Content', {
#             'fields': ('short_desc', 'description', 'benefits', 'ingredients', 'usage'),
#         }),
#         ('⚙️ Visibility', {
#             'fields': ('is_active', 'is_featured', 'order'),
#         }),
#         ('💬 WhatsApp', {
#             'fields': ('whatsapp_message',),
#         }),
#     )



#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super().formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'main_image':
#             formfield.widget.attrs.update({
#                 'role': 'uploadcare-uploader',
#                 'data-public-key': '4c3ba9de492e0e0eaddc', 
#             })
#         return formfield

#     def image_preview(self, obj):
#         if obj.main_image:
#             return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
#         return "No Image"

#     image_preview.short_description = 'Preview'





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = ('main_image', 'name', 'category', 'volume', 'badge', 'is_featured', 'is_active', 'order')
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

            # Orodha ya majina ya picha zako zote nne
            image_fields = ["main_image", "image2", "image3", "image4"]

            if db_field.name in image_fields:
                formfield.widget.attrs.update({
                    "role": "uploadcare-uploader",
                    "data-public-key": "4c3ba9de492e0e0eaddc",
                    # Unaweza kuongeza hii ili kuruhusu picha tu
                    "data-images-only": "true",
                })

            return formfield

    def image_preview(self, obj):
        html = '<div style="display: flex; gap: 5px;">'
        
        # Tunachukua picha zote kupitia ile property ya 'images' uliyotengeneza kwenye Model
        picha_zilizopo = obj.images # Hii inarudisha list ya URL zenye data
        
        if picha_zilizopo:
            for url in picha_zilizopo:
                # Tunatumia resize ndogo ili zitoshee kwenye mstari mmoja wa Admin
                cdn_url = f"https://ucarecdn.com/{url}/-/resize/x50/-/format/auto/"
                html += f'<img src="{cdn_url}" style="max-height:50px; border-radius:4px; border:1px solid #ddd;" />'
            
            html += '</div>'
            return mark_safe(html)
        
        return "No Images"

    image_preview.short_description = "Galleru Preview"
