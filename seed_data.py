import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mayila_herbal.settings')  # ← 'mayila' = folder yenye settings.py
django.setup()

from products.models import ProductCategory, Product

# CATEGORIES
cat_mens, _ = ProductCategory.objects.get_or_create(
    slug='mens-health',
    defaults={'name': "Men's Health", 'icon': '💪', 'order': 1, 'is_active': True}
)
cat_womens, _ = ProductCategory.objects.get_or_create(
    slug='womens-health',
    defaults={'name': "Women's Health", 'icon': '🌸', 'order': 2, 'is_active': True}
)
cat_diabetes, _ = ProductCategory.objects.get_or_create(
    slug='diabetes-blood-sugar',
    defaults={'name': 'Diabetes & Blood Sugar', 'icon': '🩸', 'order': 3, 'is_active': True}
)
cat_uti, _ = ProductCategory.objects.get_or_create(
    slug='urinary-kidney-health',
    defaults={'name': 'Urinary & Kidney Health', 'icon': '💧', 'order': 4, 'is_active': True}
)
print("✅ Categories done!")

# PRODUCTS
products = [
    {
        'slug': 'dumetex',
        'name': 'Dumetex',
        'category': cat_mens,
        'short_desc': 'Natural herbal solution for men facing testosterone & energy challenges.',
        'description': (
            'Dumetex is a 100% natural herbal medicine by Mayila Products, '
            'specifically formulated for men experiencing challenges related to low testosterone levels, '
            'fatigue, and reduced masculine vitality. Made from carefully selected natural herbs, '
            'it works to restore hormonal balance and boost overall male health and confidence.'
        ),
        'benefits': (
            'Boosts testosterone levels naturally\n'
            'Increases energy and stamina\n'
            'Improves hormonal balance in men\n'
            'Enhances overall masculine vitality\n'
            'Supports mental clarity and focus\n'
            '100% natural – no harmful chemicals'
        ),
        'ingredients': 'Blend of natural African medicinal herbs (proprietary formula)',
        'usage': 'Take as directed by your Mayila Herbal Clinic specialist. Shake well before use. Store in a cool, dry place away from direct sunlight.',
        'volume': '500ml',
        'targets': "Men's health, Testosterone, Low energy, Hormonal imbalance",
        'badge': 'natural',
        'is_active': True,
        'is_featured': True,
        'order': 1,
        'whatsapp_message': 'Hello, I am interested in ordering DUMETEX (500ml). Please guide me.',
    },
    {
        'slug': 'sukalini',
        'name': 'Sukalini',
        'category': cat_diabetes,
        'short_desc': 'Herbal powder that helps regulate blood sugar levels naturally.',
        'description': (
            'Sukalini is a natural herbal powder by Mayila Products designed to help the body '
            'maintain healthy blood sugar levels. Using a Kongosho Plus Formula, it supports '
            'pancreatic function and helps people living with diabetes or pre-diabetes manage '
            'their condition more effectively through natural means.'
        ),
        'benefits': (
            'Helps regulate blood sugar levels\n'
            'Supports pancreatic health (Kongosho Plus Formula)\n'
            'Reduces sugar cravings\n'
            'Improves insulin sensitivity naturally\n'
            'Suitable for both Type 1 and Type 2 diabetes support\n'
            '100% natural ingredients'
        ),
        'ingredients': 'Natural herbal blend including Kongosho-supporting plants (proprietary formula)',
        'usage': 'Dissolve the recommended amount of powder in a glass of water and drink. Best taken in the morning before meals.',
        'volume': '',
        'targets': 'Diabetes, Blood sugar, Pancreatic health',
        'badge': 'natural',
        'is_active': True,
        'is_featured': False,
        'order': 2,
        'whatsapp_message': 'Hello, I am interested in ordering SUKALINI for blood sugar support. Please guide me.',
    },
    {
        'slug': 'msuli-pawa',
        'name': 'Msuli Pawa',
        'category': cat_mens,
        'short_desc': 'Herbal remedy for men dealing with muscle weakness and reduced physical appearance.',
        'description': (
            'Msuli Pawa is a powerful 100% natural herbal tonic by Mayila Products. '
            'It targets men experiencing physical weaknesses, including muscle shrinkage and '
            'reduced physical presence. The formula is designed to restore masculine strength, '
            'improve muscle tone, and boost self-confidence naturally.'
        ),
        'benefits': (
            'Helps restore muscle strength and tone\n'
            'Addresses shrinkage and reduced size concerns\n'
            'Boosts masculine confidence and vitality\n'
            'Improves blood circulation to muscles\n'
            'All-natural herbal formula – safe for regular use'
        ),
        'ingredients': 'Proprietary blend of natural herbs and plant extracts',
        'usage': 'Take the recommended dose as instructed by Mayila Herbal Clinic. For best results, maintain consistent use over the prescribed period.',
        'volume': '500ml',
        'targets': "Men's health, Muscle strength, Physical vitality",
        'badge': 'natural',
        'is_active': True,
        'is_featured': True,
        'order': 3,
        'whatsapp_message': 'Hello, I am interested in ordering MSULI PAWA (500ml). Please guide me.',
    },
    {
        'slug': 'sperm-builder',
        'name': 'Sperm Builder',
        'category': cat_mens,
        'short_desc': 'Increases sperm count and improves male reproductive health naturally.',
        'description': (
            'Sperm Builder by Mayila Products is a 100% natural supplement specifically formulated '
            'to increase sperm count, improve sperm motility, and support overall male reproductive health. '
            'It is ideal for men facing fertility challenges or those looking to strengthen their '
            'reproductive system using natural herbal medicine.'
        ),
        'benefits': (
            'Significantly increases sperm count\n'
            'Improves sperm motility and quality\n'
            'Supports overall male reproductive health\n'
            'Boosts testosterone naturally\n'
            'Helps with male infertility concerns\n'
            '100% natural formula'
        ),
        'ingredients': 'Natural herbal blend formulated for male reproductive support (proprietary)',
        'usage': 'Take as directed by your Mayila Herbal Clinic specialist. Consistent use over the recommended period is essential for best results.',
        'volume': '500ml',
        'targets': "Men's health, Fertility, Sperm count, Reproductive health",
        'badge': 'bestseller',
        'is_active': True,
        'is_featured': True,
        'order': 4,
        'whatsapp_message': 'Hello, I am interested in ordering SPERM BUILDER (500ml). Please guide me.',
    },
    {
        'slug': 'master-clean',
        'name': 'Master Clean',
        'category': cat_uti,
        'short_desc': 'The ultimate herbal solution for stubborn UTI (Urinary Tract Infections).',
        'description': (
            'Master Clean by Mayila Products is a powerful natural liquid medicine that targets '
            'Urinary Tract Infections (UTI) at the root. Unlike conventional treatments that may '
            'only provide temporary relief, Master Clean works from the first day of use to '
            'clear the infection and restore urinary tract health. Suitable for both men and women.'
        ),
        'benefits': (
            'Eliminates UTI-causing bacteria naturally\n'
            'Results visible from the first day of use\n'
            'Cleanses the urinary tract and kidneys\n'
            'Reduces burning and pain during urination\n'
            'Prevents recurrence of UTI\n'
            'Safe for both men and women'
        ),
        'ingredients': 'Natural herbal extracts with urinary cleansing properties (Easo Care formula)',
        'usage': 'Take as instructed – results begin from the day you start using the medicine. Contact: 0676718040.',
        'volume': '',
        'targets': 'UTI, Urinary tract infection, Kidney health, Both men and women',
        'badge': 'bestseller',
        'is_active': True,
        'is_featured': True,
        'order': 5,
        'whatsapp_message': 'Hello, I am interested in ordering MASTER CLEAN for UTI treatment. Please guide me.',
    },
    {
        'slug': 'mvyei',
        'name': 'Mvyei',
        'category': cat_womens,
        'short_desc': "Natural herbal tonic supporting women's reproductive and uterine health.",
        'description': (
            'Mvyei is a 100% natural herbal liquid by Mayila Products designed to support and '
            "strengthen women's reproductive system. It helps address common reproductive health "
            'challenges in women including uterine issues, ovarian health, and general gynecological wellness.'
        ),
        'benefits': (
            'Supports uterine and ovarian health\n'
            "Helps with women's reproductive system disorders\n"
            'Balances female hormones naturally\n'
            'Promotes overall gynecological wellness\n'
            'Safe and natural herbal formula\n'
            '400ml – good value for a full treatment course'
        ),
        'ingredients': 'Proprietary blend of natural herbs supporting female reproductive health',
        'usage': 'Take as recommended by Mayila Herbal Clinic specialist. Contact: 0762 519 040 / 0676 718 040.',
        'volume': '400ml',
        'targets': "Women's health, Reproductive health, Uterine health, Ovarian health",
        'badge': 'natural',
        'is_active': True,
        'is_featured': True,
        'order': 6,
        'whatsapp_message': "Hello, I am interested in ordering MVYEI (400ml) for women's health. Please guide me.",
    },
    {
        'slug': 'mdindadinda',
        'name': 'Mdindadinda',
        'category': cat_mens,
        'short_desc': "The ultimate natural herbal medicine for men's strength and masculine power.",
        'description': (
            'Mdindadinda – Kiboko ya Nguvu za Kiume – is a premium natural herbal medicine '
            'by Mayila Products, crafted exclusively for adult men seeking to restore and enhance '
            'their masculine strength and vitality. With its powerful all-natural formula, '
            'Mdindadinda addresses the root causes of male weakness and helps men regain '
            'their confidence and physical performance.'
        ),
        'benefits': (
            'Restores and boosts male strength and vigor\n'
            'Enhances physical and sexual performance\n'
            'Improves energy levels and stamina\n'
            'Supports healthy testosterone production\n'
            '100% natural – Dawa ya Asili\n'
            'For adult men only (Kwa matumizi ya watu wazima)'
        ),
        'ingredients': 'Premium blend of natural African medicinal herbs (proprietary formula)',
        'usage': 'For adult men only. Take as directed. Not for children (Mbali na watoto). Store in a cool dry place.',
        'volume': '',
        'targets': "Men's health, Strength, Vitality, Sexual health, Energy",
        'badge': 'bestseller',
        'is_active': True,
        'is_featured': False,
        'order': 7,
        'whatsapp_message': "Hello, I am interested in ordering MDINDADINDA for men's strength. Please guide me.",
    },
]

for data in products:
    obj, created = Product.objects.get_or_create(slug=data['slug'], defaults=data)
    status = "✅ Created" if created else "⚠️  Already exists"
    print(f"{status}: {obj.name}")

print(f"\n📦 Total products: {Product.objects.count()}")
print(f"📂 Total categories: {ProductCategory.objects.count()}")