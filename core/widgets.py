# core/widgets.py
from django import forms

class UploadcareWidget(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {
            'role': 'uploadcare-uploader',
            'data-public-key': '4c3ba9de492e0e0eaddc',
            'data-images-only': 'true',
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
    
    class Media:
        js = ['https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js']