from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    name       = models.CharField(max_length=100)
    slug       = models.SlugField(unique=True)
    icon       = models.CharField(max_length=50, blank=True, help_text='Emoji or icon class')
    order      = models.PositiveIntegerField(default=0)
    is_active  = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    BADGE_CHOICES = [
        ('bestseller', '🔥 Best Seller'),
        ('new', '✨ New'),
        ('natural', '🌿 100% Natural'),
        ('featured', '⭐ Featured'),
        ('', 'No Badge'),
    ]

    name            = models.CharField(max_length=200)
    slug            = models.SlugField(unique=True)
    category        = models.ForeignKey('ProductCategory', on_delete=models.SET_NULL, null=True, blank=True, related_name='products')

    main_image      = models.CharField(blank=True, help_text="Uploadcare CDN URL - main image")
    image2          = models.CharField(max_length=255, blank=True, null=True)
    image3          = models.CharField(max_length=255, blank=True, null=True)
    image4          = models.CharField(max_length=255, blank=True, null=True)

    short_desc      = models.CharField(max_length=300, help_text='Short tagline shown on cards')
    description     = models.TextField(help_text='Full product description')
    benefits        = models.TextField(blank=True, help_text='One benefit per line')
    ingredients     = models.TextField(blank=True)
    usage           = models.TextField(blank=True, help_text='How to use / Jinsi ya kutumia')
    volume          = models.CharField(max_length=50, blank=True, help_text='e.g. 500ml, 400ml')
    targets         = models.CharField(max_length=300, blank=True, help_text="e.g. Men's health, Women's health, Diabetes")

    badge           = models.CharField(max_length=20, choices=BADGE_CHOICES, blank=True)
    is_active       = models.BooleanField(default=True)
    is_featured     = models.BooleanField(default=False, help_text='Show in hero slider')
    order           = models.PositiveIntegerField(default=0)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    whatsapp_message = models.CharField(max_length=300, blank=True, help_text='Custom WhatsApp message for this product. Leave blank for default.')
    price           = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, help_text='Bei ya bidhaa kwa TZS (optional — inaonekana kwenye Google rich results)')

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_benefits_list(self):
        return [b.strip() for b in self.benefits.splitlines() if b.strip()]

    @property
    def images(self):
        imgs = []
        for url in [self.main_image, self.image2, self.image3, self.image4]:
            if url:
                imgs.append(url)
        return imgs

    def get_image_url(self):
        if not self.main_image:
            return ""
        base = self.main_image.rstrip('/')
        if base.startswith('http'):
            return f"{base}/-/format/jpg/-/quality/smart/"
        return f"https://ucarecdn.com/{base}/-/format/jpg/-/quality/smart/"

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def get_whatsapp_msg(self):
        if self.whatsapp_message:
            return self.whatsapp_message
        return f"Hello! I am interested in {self.name}."

    def get_meta_description(self):
        """SEO description kwa kila bidhaa — inakwenda kwenye Google snippet."""
        if self.short_desc:
            return self.short_desc
        if self.description:
            import re
            clean = re.sub(r'<[^>]+>', '', self.description)
            return clean[:160].strip()
        return f"{self.name} — Natural herbal product from Mayila Herbal Clinic, Mbeya Tanzania."

    def get_og_image_url(self):
        """Open Graph image URL (1200x630) kwa social sharing."""
        if not self.main_image:
            return ""
        # main_image inaweza kuwa full URL au UUID tu
        base = self.main_image.rstrip('/')
        if base.startswith('http'):
            # Full URL tayari — ongeza transformations tu
            return f"{base}/-/resize/1200x630/-/format/jpg/-/quality/smart/"
        else:
            # UUID tu — ongeza ucarecdn.com prefix
            return f"https://ucarecdn.com/{base}/-/resize/1200x630/-/format/jpg/-/quality/smart/"
