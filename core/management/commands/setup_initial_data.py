from django.core.management.base import BaseCommand
from core.models import SiteSettings, FAQ, Announcement
from products.models import ProductCategory


class Command(BaseCommand):
    help = 'Setup initial site data for Mayila Herbal Clinic'

    def handle(self, *args, **kwargs):
        # Site Settings
        site, created = SiteSettings.objects.get_or_create(pk=1)
        if created:
            self.stdout.write(self.style.SUCCESS('✅ Site Settings created with defaults'))
        else:
            self.stdout.write('ℹ️  Site Settings already exist')

        # Categories
        cats = [
            {'name': "Men's Health", 'slug': 'wanaume', 'icon': '💪', 'order': 1},
            {'name': "Women's Health", 'slug': 'wanawake', 'icon': '🌸', 'order': 2},
            {'name': 'Diabetes', 'slug': 'sukari', 'icon': '🩺', 'order': 3},
            {'name': 'UTI & Kidney', 'slug': 'uti', 'icon': '🫀', 'order': 4},
        ]
        for c in cats:
            obj, created = ProductCategory.objects.get_or_create(slug=c['slug'], defaults=c)
            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Category '{c['name']}' created"))

        # FAQs
        faqs = [
            ('Je, bidhaa zenu ni salama?', 'Ndiyo, bidhaa zetu zote ni za asili 100% na zimesajiliwa na Wizara ya Afya Tanzania. Hana madhara makubwa kiafya.', 1),
            ('Ninaweza kupata bidhaa vipi?', 'Unaweza kutupigia simu, kutuma WhatsApp, au kuja moja kwa moja ofisini kwetu Mbalizi, Mbeya. Tunatoa delivery.', 2),
            ('Matokeo yanaonekana lini?', 'Inategemea hali ya kila mtu. Wateja wengi wanaona matokeo ndani ya wiki 2-4 za matumizi ya mara kwa mara.', 3),
            ('Je, mna delivery?', 'Ndiyo! Tunatoa huduma ya delivery Tanzania nzima. Wasiliana nasi kupitia WhatsApp kwa maelezo zaidi.', 4),
        ]
        for q, a, o in faqs:
            FAQ.objects.get_or_create(question=q, defaults={'answer': a, 'order': o})
        self.stdout.write(self.style.SUCCESS('✅ FAQs created'))

        # Announcement
        Announcement.objects.get_or_create(
            text='🌿 Free consultation for new customers! Call +255676718040 today.',
            defaults={'is_active': True, 'bg_color': '#1a5c2e', 'text_color': '#ffffff'}
        )
        self.stdout.write(self.style.SUCCESS('✅ Announcement created'))
        self.stdout.write(self.style.SUCCESS('\n🎉 Initial data setup complete! Run: python manage.py createsuperuser'))
