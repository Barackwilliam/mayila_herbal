# products/forms.py
from django import forms
from .models import Product, ProductCategory
from core.widgets import UploadcareWidget  # ← Import from core


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
            'main_image': UploadcareWidget(),
            'image2': UploadcareWidget(),
            'image3': UploadcareWidget(),
            'image4': UploadcareWidget(),
        }

    class Media:
        js = ['https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js']