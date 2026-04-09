# core/models.py
from django.db import models

UCARECDN_BASE = 'https://ucarecdn.com'

def uc_url(uuid_val, transform=''):
    if not uuid_val:
        return ''
    return f"{UCARECDN_BASE}/{uuid_val}/{transform}"


class SiteSettings(models.Model):
    """Single-row table — controls EVERYTHING on the website from admin."""

    # Brand Identity
    site_name        = models.CharField(max_length=200, default='Mayila Herbal Clinic')
    tagline          = models.CharField(max_length=300, default='Tiba za Asili • Natural Healing')
    logo             = models.CharField(max_length=255, blank=True, null=True, help_text='Uploadcare UUID')
    favicon          = models.CharField(max_length=255, blank=True, null=True)
    hero_bg_image    = models.CharField(max_length=255, blank=True, null=True)
    about_image      = models.CharField(max_length=255, blank=True, null=True)

    # Colors (CSS Variables)
    primary_color    = models.CharField(max_length=20, default='#1a5c2e', help_text='Main green color')
    secondary_color  = models.CharField(max_length=20, default='#c9a84c', help_text='Gold accent color')
    dark_color       = models.CharField(max_length=20, default='#0d1f0f')
    light_color      = models.CharField(max_length=20, default='#f5f0e8')
    text_color       = models.CharField(max_length=20, default='#1a1a1a')

    # Hero Section
    hero_title       = models.CharField(max_length=300, default="Nature's Power, Your Health")
    hero_subtitle    = models.TextField(default='100% Natural Herbal Products — Certified & Trusted\nBidhaa za Asili Zilizo Salama na Zenye Ufanisi')
    hero_cta_text    = models.CharField(max_length=100, default='Explore Products')
    hero_cta2_text   = models.CharField(max_length=100, default='Contact Us')

    # About Section
    about_title      = models.CharField(max_length=200, default='About Mayila Herbal Clinic')
    about_text       = models.TextField(default='Mayila Herbal Clinic ni kituo cha tiba za asili kilichopo Mbalizi, Mbeya, Tanzania.\n\nKituo kimesajiliwa na Wizara ya Afya chini ya namba ya usajili MBY/136/TP/00112/2023, na kinajihusisha na utoaji wa tiba za asili pamoja na ushauri wa kiafya kwa watu wenye changamoto mbalimbali za kiafya.\n\nTaasisi hii ilianzishwa kwa lengo la kusaidia jamii kupata tiba mbadala iliyo salama, nafuu, na yenye matokeo chanya bila madhara makubwa kiafya.')
    registration_no  = models.CharField(max_length=100, default='MBY/136/TP/00112/2023')

    # Vision & Mission
    vision_text      = models.TextField(default='Kuunda jamii yenye afya bora kupitia tiba za asili salama, nafuu na zenye ufanisi.')
    mission_text     = models.TextField(default='• Kutoa tiba za asili salama na zenye ufanisi kwa wagonjwa.\n• Kutoa ushauri wa kiafya wa karibu na wa kibinafsi.\n• Kujenga uaminifu na matokeo chanya kwa wagonjwa.\n• Kuendeleza elimu ya tiba za asili kwa jamii.')

    # Stats
    stat1_number     = models.CharField(max_length=20, default='7+')
    stat1_label      = models.CharField(max_length=100, default='Herbal Products')
    stat2_number     = models.CharField(max_length=20, default='1000+')
    stat2_label      = models.CharField(max_length=100, default='Happy Clients')
    stat3_number     = models.CharField(max_length=20, default='100%')
    stat3_label      = models.CharField(max_length=100, default='Natural Ingredients')
    stat4_number     = models.CharField(max_length=20, default='2023')
    stat4_label      = models.CharField(max_length=100, default='Est. Year')

    # Contact Information
    phone1           = models.CharField(max_length=30, default='+255676718040')
    phone2           = models.CharField(max_length=30, blank=True, default='+255762518040')
    email            = models.EmailField(blank=True, default='mayilaherbalclinic@gmail.com')
    whatsapp_number  = models.CharField(max_length=30, default='+255676718040', help_text='Include country code e.g. +255676718040')
    whatsapp_message = models.CharField(max_length=300, default='Hello! I am interested in your herbal products.')
    location         = models.CharField(max_length=300, default='Mbalizi, Mbeya, Tanzania')
    google_maps_embed = models.TextField(blank=True, help_text='Paste full Google Maps embed iframe code')

    # Social Media
    facebook_url     = models.URLField(blank=True)
    instagram_url    = models.URLField(blank=True)
    tiktok_url       = models.URLField(blank=True)
    youtube_url      = models.URLField(blank=True)
    twitter_url      = models.URLField(blank=True)

    # Footer
    footer_text      = models.TextField(default='© Mayila Herbal Clinic. All rights reserved. | Mbalizi, Mbeya, Tanzania')
    footer_tagline   = models.CharField(max_length=300, default='Afya ni Hazina — Health is Wealth')

    # SEO
    meta_description = models.TextField(default='Mayila Herbal Clinic — Natural herbal products from Mbeya, Tanzania. 100% natural, safe and effective herbal medicine.')
    meta_keywords    = models.TextField(default='herbal clinic, tiba za asili, Mbeya, Tanzania, natural medicine, mdindadinda, mvyei, msuli pawa, dumetex, master clean')

    # Section Labels
    products_section_title    = models.CharField(max_length=200, default='Our Products')
    products_section_subtitle = models.CharField(max_length=300, default='Bidhaa Zetu za Asili — 100% Natural & Certified')
    videos_section_title      = models.CharField(max_length=200, default='Product Advertisements')
    videos_section_subtitle   = models.CharField(max_length=300, default='Watch our latest product videos — Tazama matangazo yetu')
    testimonials_title        = models.CharField(max_length=200, default='What Our Clients Say')

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return f'Site Settings — {self.site_name}'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    # ============ EXISTING METHODS (Zilizopo tayari) ============
    def get_logo_url(self):
        return uc_url(self.logo, '-/resize/200x/-/format/webp/-/quality/smart/')

    def get_favicon_url(self):
        return uc_url(self.favicon, '-/resize/64x64/-/format/webp/')

    def get_hero_bg_url(self):
        return uc_url(self.hero_bg_image, '-/resize/2000x/-/format/webp/-/quality/smart/')

    def get_about_image_url(self):
        return uc_url(self.about_image, '-/resize/800x/-/format/webp/-/quality/smart/')

    # ============ NEW METHODS (Kama Hiker Store) ============
    
    def get_image_url(self, field_name, width=None, height=None, transform_extra=''):
        """
        Generic method to get any image URL with transformations
        Usage: 
            site.get_image_url('logo', width=200)
            site.get_image_url('hero_bg_image', width=1920)
            site.get_image_url('about_image', width=800, height=600)
        """
        # Get the field value
        uuid_val = getattr(self, field_name, None)
        
        if not uuid_val:
            return ""
        
        # Build transformations
        transforms = []
        if transform_extra:
            transforms.append(transform_extra)
        if width or height:
            if width and height:
                transforms.append(f"-/resize/{width}x{height}/")
            elif width:
                transforms.append(f"-/resize/{width}x/")
            elif height:
                transforms.append(f"-/resize/x{height}/")
        
        transforms.append("-/format/webp/")
        transforms.append("-/quality/smart/")
        
        transform_str = ' '.join(transforms).strip()
        if transform_str:
            return f"{UCARECDN_BASE}/{uuid_val}/{transform_str}"
        return f"{UCARECDN_BASE}/{uuid_val}"

    def get_logo_thumbnail(self):
        """Logo thumbnail (smaller)"""
        return self.get_image_url('logo', width=100, height=100)

    def get_hero_bg_large(self):
        """Hero background - large desktop version"""
        return self.get_image_url('hero_bg_image', width=1920)

    def get_hero_bg_mobile(self):
        """Hero background - mobile optimized"""
        return self.get_image_url('hero_bg_image', width=768)

    def get_about_image_thumbnail(self):
        """About section image thumbnail"""
        return self.get_image_url('about_image', width=400, height=400)

    def get_og_image_url(self):
        """Open Graph image for social media sharing (uses hero_bg_image)"""
        if self.hero_bg_image:
            return f"{UCARECDN_BASE}/{self.hero_bg_image}/-/resize/1200x630/-/format/webp/"
        return ""

    @property
    def all_images(self):
        """Returns list of all image UUIDs that exist in SiteSettings"""
        imgs = []
        for field in ['logo', 'favicon', 'hero_bg_image', 'about_image']:
            val = getattr(self, field, None)
            if val:
                imgs.append(val)
        return imgs


class Testimonial(models.Model):
    # ... (haujabadilisha, unachokipa chochote)
    name        = models.CharField(max_length=100)
    location    = models.CharField(max_length=150, blank=True)
    message     = models.TextField()
    photo       = models.CharField(max_length=255, blank=True, null=True)
    product     = models.CharField(max_length=100, blank=True, help_text='Which product helped them?')
    rating      = models.PositiveSmallIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f'{self.name} — ★{self.rating}'
    
    def get_photo_url(self):
        return uc_url(self.photo, '-/resize/88x/-/format/webp/-/quality/smart/')

    # Ongeza hii kwa testimonial pia
    def get_photo_thumbnail(self):
        return self.get_photo_url()


class FAQ(models.Model):
    # ... (haujabadilisha)
    question   = models.CharField(max_length=300)
    answer     = models.TextField()
    order      = models.PositiveIntegerField(default=0)
    is_active  = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question


class Announcement(models.Model):
    # ... (haujabadilisha)
    text       = models.CharField(max_length=300)
    is_active  = models.BooleanField(default=True)
    bg_color   = models.CharField(max_length=20, default='#1a5c2e')
    text_color = models.CharField(max_length=20, default='#ffffff')
    link       = models.URLField(blank=True)
    link_text  = models.CharField(max_length=80, blank=True)

    class Meta:
        verbose_name = 'Announcement Banner'
        verbose_name_plural = 'Announcement Banners'

    def __str__(self):
        return self.text[:60]