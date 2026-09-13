"""
Downloads every product image still hosted on Uploadcare and re-uploads
it to the Supabase Storage bucket, updating the Product row in place.

Usage:
    python manage.py migrate_images_to_supabase            # do the migration
    python manage.py migrate_images_to_supabase --dry-run   # preview only
"""
from django.core.management.base import BaseCommand

from core.supabase_storage import download_uploadcare, is_supabase_url, upload_bytes
from products.models import Product

FIELDS = ['main_image', 'image2', 'image3', 'image4']


class Command(BaseCommand):
    help = "Migrates existing Uploadcare product images to the Supabase Storage bucket."

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run', action='store_true',
            help="Show what would be migrated without uploading or saving anything.",
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        products = Product.objects.all()

        total_slots = migrated = skipped = failed = 0

        for product in products:
            changed_fields = []

            for field in FIELDS:
                value = getattr(product, field)
                total_slots += 1

                if not value:
                    skipped += 1
                    continue

                if is_supabase_url(value):
                    # Already migrated in a previous run
                    skipped += 1
                    continue

                data, content_type, error = download_uploadcare(value)
                if not data:
                    self.stderr.write(self.style.WARNING(
                        f"  ✗ {product.name} / {field}: could not download {value} ({error})"
                    ))
                    failed += 1
                    continue

                ext = (content_type or 'image/jpeg').split('/')[-1]
                filename = f"{product.slug}-{field}.{ext}"

                if dry_run:
                    self.stdout.write(f"  [dry-run] {product.name} / {field}: would upload {len(data)} bytes")
                    migrated += 1
                    continue

                new_url = upload_bytes(data, filename, content_type)
                setattr(product, field, new_url)
                changed_fields.append(field)
                migrated += 1
                self.stdout.write(self.style.SUCCESS(f"  ✓ {product.name} / {field} → {new_url}"))

            if changed_fields and not dry_run:
                product.save(update_fields=changed_fields)

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. Checked {total_slots} image slots — migrated {migrated}, "
            f"skipped {skipped} (empty/already migrated), failed {failed}."
        ))
        if failed:
            self.stdout.write(self.style.WARNING(
                "Some images failed to download — check the URLs above; "
                "they may need to be re-uploaded manually from the admin."
            ))
