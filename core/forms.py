
# core/forms.py
from django import forms
from .models import SiteSettings, Testimonial
from .widgets import UploadcareWidget  # ← Import custom widget


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'logo': UploadcareWidget(),
            'favicon': UploadcareWidget(),
            'hero_bg_image': UploadcareWidget(),
            'about_image': UploadcareWidget(),
        }

    class Media:
        js = ['https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js']


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        widgets = {
            'photo': UploadcareWidget(),
        }

    class Media:
        js = ['https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js']