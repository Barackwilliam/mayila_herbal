from products.models import Product

prices = {
    'mdindadinda':         25000,
    'chidume-halisi':      25000,
    'msuli-pawa':          30000,
    'gastalini':           30000,
    'master-clean':        25000,
    'sperm-builder':       50000,
    'dumetex':             50000,
    'mvyei':               50000,
    'sukalini':            50000,
    'mayipress':           50000,
    'preshalini':          50000,
    'mayboost':            50000,
    'mayila-slimming-tea': 35000,
    'maygast':             20000,
}

updated = 0
not_found = []

for slug, price in prices.items():
    try:
        p = Product.objects.get(slug=slug)
        p.price = price
        p.save(update_fields=['price'])
        print("OK: " + p.name + " -> TZS " + str(price))
        updated += 1
    except Product.DoesNotExist:
        print("NOT FOUND: " + slug)
        not_found.append(slug)

print("Done. Updated: " + str(updated) + " products")
if not_found:
    print("Not found: " + str(not_found))