# products/forms.py
from django import forms
from tinymce.widgets import TinyMCE
from .models import Product, ProductCategory
from core.supabase_storage import upload_django_file


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
    # ── Image fields — real file uploads, sent straight to Supabase
    # Storage. The underlying model fields (main_image, image2, image3,
    # image4) stay as CharField URLs — these extra fields just collect
    # a new file when the admin wants to replace an image; see save().
    main_image_upload = forms.ImageField(required=False, label='Picha kuu — pakia mpya (Supabase)')
    image2_upload     = forms.ImageField(required=False, label='Picha ya 2 — pakia mpya')
    image3_upload     = forms.ImageField(required=False, label='Picha ya 3 — pakia mpya')
    image4_upload     = forms.ImageField(required=False, label='Picha ya 4 — pakia mpya')

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            # ── Image URL fields — hidden; kept in sync by save() below ──
            'main_image': forms.HiddenInput(),
            'image2':     forms.HiddenInput(),
            'image3':     forms.HiddenInput(),
            'image4':     forms.HiddenInput(),

            # ── Text fields — TinyMCE ─────────────────────────────────────
            'description': TinyMCE(attrs={'cols': 80, 'rows': 20}),
            'ingredients':  TinyMCE(attrs={'cols': 80, 'rows': 15}),
            'usage':        TinyMCE(attrs={'cols': 80, 'rows': 15}),
            'benefits':     TinyMCE(
                attrs={'cols': 80, 'rows': 10},
                mce_attrs=TINYMCE_BENEFITS_CONFIG,
            ),
        }

    def save(self, commit=True):
        upload_map = {
            'main_image': 'main_image_upload',
            'image2':     'image2_upload',
            'image3':     'image3_upload',
            'image4':     'image4_upload',
        }
        for model_field, upload_field in upload_map.items():
            uploaded_file = self.cleaned_data.get(upload_field)
            if uploaded_file:
                url = upload_django_file(uploaded_file)
                setattr(self.instance, model_field, url)
        return super().save(commit=commit)