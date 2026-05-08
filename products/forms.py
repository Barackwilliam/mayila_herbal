# products/forms.py
from django import forms
from tinymce.widgets import TinyMCE
from .models import Product, ProductCategory
from core.widgets import UploadcareWidget


# Config ndogo kwa benefits — lists tu, bila formatting nyingi
TINYMCE_BENEFITS_CONFIG = {
    'height': 220,
    'menubar': False,
    'plugins': ['lists', 'paste'],
    'toolbar': 'bullist numlist | removeformat | pastetext',
    'paste_as_text': True,
    'content_style': (
        'body { font-family: sans-serif; font-size: 14px; '
        'line-height: 1.8; color: #333; padding: 8px; }'
    ),
}


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    class Media:
        js = ['https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js']


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            # ── Image fields — Uploadcare (bila mabadiliko) ──────────────
            'main_image': UploadcareWidget(),
            'image2':     UploadcareWidget(),
            'image3':     UploadcareWidget(),
            'image4':     UploadcareWidget(),

            # ── Text fields — TinyMCE (mpya) ─────────────────────────────
            'description': TinyMCE(attrs={'cols': 80, 'rows': 20}),
            'ingredients':  TinyMCE(attrs={'cols': 80, 'rows': 15}),
            'usage':        TinyMCE(attrs={'cols': 80, 'rows': 15}),
            'benefits':     TinyMCE(
                attrs={'cols': 80, 'rows': 10},
                mce_attrs=TINYMCE_BENEFITS_CONFIG,
            ),
        }

    class Media:
        js = ['https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js']