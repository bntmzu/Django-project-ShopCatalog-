import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.conf import settings
import os


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        fixtures_path = os.path.join(settings.BASE_DIR, 'catalog_data_utf8.json')

        with open(fixtures_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            model = item['model']
            fields = item['fields']
            if model == 'catalog.category':
                Category.objects.create(
                    pk=item['pk'],
                    name=fields['name'],
                    description=fields['description']
                )

        for item in data:
            model = item['model']
            fields = item['fields']
            if model == 'catalog.product':
                category = Category.objects.get(pk=fields['category'])
                Product.objects.create(
                    pk=item['pk'],
                    name=fields['name'],
                    description=fields['description'],
                    category=category,
                    price=fields['price'],
                    created_at=fields['created_at'],
                    updated_at=fields['updated_at']
                )

        self.stdout.write(self.style.SUCCESS('Database successfully populated with fixture data'))
