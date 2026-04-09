from django.contrib import admin
from django.utils.html import format_html
from .forms import SiteSettingsForm, TestimonialForm
from .models import SiteSettings, Testimonial, FAQ, Announcement


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsForm
    fieldsets = (
        ('🏢 Brand Identity', {
            'fields': ('site_name', 'tagline', 'logo', 'favicon'),
        }),
        ('🎨 Colors (CSS Variables)', {
            'fields': ('primary_color', 'secondary_color', 'dark_color', 'light_color', 'text_color'),
            'description': 'These colors apply across the whole website instantly.',
        }),
        ('🦸 Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_bg_image', 'hero_cta_text', 'hero_cta2_text'),
        }),
        ('ℹ️ About Section', {
            'fields': ('about_title', 'about_text', 'about_image', 'registration_no'),
        }),
        ('🎯 Vision & Mission', {
            'fields': ('vision_text', 'mission_text'),
        }),
        ('📊 Stats / Numbers', {
            'fields': (
                ('stat1_number', 'stat1_label'),
                ('stat2_number', 'stat2_label'),
                ('stat3_number', 'stat3_label'),
                ('stat4_number', 'stat4_label'),
            ),
        }),
        ('📦 Products Section Labels', {
            'fields': ('products_section_title', 'products_section_subtitle'),
        }),
        ('🎬 Videos Section Labels', {
            'fields': ('videos_section_title', 'videos_section_subtitle'),
        }),
        ('💬 Testimonials Section', {
            'fields': ('testimonials_title',),
        }),
        ('📞 Contact Information', {
            'fields': ('phone1', 'phone2', 'email', 'location', 'google_maps_embed'),
        }),
        ('💬 WhatsApp Settings', {
            'fields': ('whatsapp_number', 'whatsapp_message'),
        }),
        ('📱 Social Media Links', {
            'fields': ('facebook_url', 'instagram_url', 'tiktok_url', 'youtube_url', 'twitter_url'),
        }),
        ('🔻 Footer', {
            'fields': ('footer_text', 'footer_tagline'),
        }),
        ('🔍 SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )

    # Ongeza preview ya picha kwenye list_display
    list_display = ['logo_preview', 'site_name', 'hero_cta_text', 'is_configured']
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html(f'<img src="{obj.get_logo_url()}" style="max-height:40px; border-radius:4px;" />')
        return "No Logo"
    logo_preview.short_description = 'Logo'

    def is_configured(self, obj):
        return "✅" if obj.logo else "⚠️"
    is_configured.short_description = 'Status'

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    form = TestimonialForm  # ← HAPA
    list_display  = ('name', 'location', 'product', 'rating', 'is_active', 'order')
    list_editable = ('is_active', 'order', 'rating')
    list_filter   = ('is_active', 'rating')
    search_fields = ('name', 'message', 'product')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display  = ('question', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display  = ('text', 'is_active', 'bg_color')
    list_editable = ('is_active',)
