from django.core.management.base import BaseCommand
from tyres.models import RimModel, RimVariant

class Command(BaseCommand):
    help = 'Seeds the database with ONLY existing rims (9), matching available images.'

    def handle(self, *args, **kwargs):
        rims_data = [
            {
                'brand': 'BBS',
                'name': 'CH-R',
                'description': 'Легендарные немецкие диски с классическим дизайном и высокой прочностью. Идеальны для премиальных авто.',
                'image': 'rims/variants/bbschr.jpg',
                'variants': [
                    {'diameter': 18, 'width': 8.0, 'bolt_pattern': '5x120', 'offset': 35, 'dia': 72.6, 'color': 'Silver', 'material': 'Cast Aluminum', 'price': 50000, 'stock': 5},
                ]
            },
            {
                'brand': 'Work',
                'name': 'Emotion CR Kai',
                'description': 'Японские диски для тюнинга с агрессивным дизайном. Отличный выбор для спортивных авто.',
                'image': 'rims/variants/worksrkai.jpg',
                'variants': [
                    {'diameter': 18, 'width': 9.5, 'bolt_pattern': '5x114.3', 'offset': 30, 'dia': 73.1, 'color': 'White', 'material': 'Cast Aluminum', 'price': 24000, 'stock': 8},
                ]
            },
            {
                'brand': 'Vossen',
                'name': 'HF-3',
                'description': 'Премиальные диски с уникальным дизайном для люксовых автомобилей. Легкость и прочность.',
                'image': 'rims/variants/vossenhf3.jpg',
                'variants': [
                    {'diameter': 20, 'width': 9.0, 'bolt_pattern': '5x112', 'offset': 32, 'dia': 66.6, 'color': 'Gloss Black', 'material': 'Hybrid Forged', 'price': 40000, 'stock': 4},
                ]
            },
            {
                'brand': 'Rotiform',
                'name': 'LAS-R',
                'description': 'Стильные диски с агрессивным дизайном, популярные в stance-культуре.',
                'image': 'rims/variants/lasr.jpg',
                'variants': [
                    {'diameter': 19, 'width': 8.5, 'bolt_pattern': '5x112', 'offset': 35, 'dia': 57.1, 'color': 'Silver Machined', 'material': 'Cast Aluminum', 'price': 25000, 'stock': 6},
                ]
            },
            {
                'brand': 'Rial',
                'name': 'Lucca',
                'description': 'Элегантные немецкие диски с 10 спицами. Отличное соотношение цена/качество.',
                'image': 'rims/variants/riallucca.jpg',
                'variants': [
                    {'diameter': 18, 'width': 8.0, 'bolt_pattern': '5x112', 'offset': 45, 'dia': 66.6, 'color': 'Silver', 'material': 'Cast Aluminum', 'price': 16000, 'stock': 7},
                ]
            },
            {
                'brand': 'Rays',
                'name': 'TE37',
                'description': 'Культовые кованые японские диски. Минимальный вес и максимальная прочность.',
                'image': 'rims/variants/TE37.png',
                'variants': [
                    {'diameter': 18, 'width': 9.5, 'bolt_pattern': '5x114.3', 'offset': 12, 'dia': 73.1, 'color': 'Bronze', 'material': 'Forged Aluminum', 'price': 70000, 'stock': 3},
                ]
            },
            {
                'brand': 'OZ Racing',
                'name': 'Ultraleggera',
                'description': 'Легкосплавные диски с уникальным дизайном и минимальным весом.',
                'image': 'rims/variants/ozracingultraleggera.jpg',
                'variants': [
                    {'diameter': 18, 'width': 8.0, 'bolt_pattern': '5x112', 'offset': 48, 'dia': 66.6, 'color': 'Silver', 'material': 'Cast Aluminum', 'price': 15000, 'stock': 10},
                ]
            },
            {
                'brand': 'Enkei',
                'name': 'RPF1',
                'description': 'Легкие гоночные диски с классическим дизайном. Минимальный вес и высокая прочность.',
                'image': 'rims/variants/enkeirpf1.jpg',
                'variants': [
                    {'diameter': 17, 'width': 8.0, 'bolt_pattern': '5x100', 'offset': 45, 'dia': 73.1, 'color': 'Silver', 'material': 'Cast Aluminum', 'price': 16000, 'stock': 8},
                ]
            },
            {
                'brand': 'Dotz',
                'name': 'Hanzo',
                'description': 'Агрессивный дизайн с острыми спицами. Стильный внешний вид для современных авто.',
                'image': 'rims/variants/dotzhanzo.jpg',
                'variants': [
                    {'diameter': 19, 'width': 8.5, 'bolt_pattern': '5x114.3', 'offset': 40, 'dia': 73.1, 'color': 'Black', 'material': 'Cast Aluminum', 'price': 22000, 'stock': 5},
                ]
            },
        ]

        for rim_data in rims_data:
            rim_model = RimModel.objects.create(
                brand=rim_data['brand'],
                name=rim_data['name'],
                description=rim_data['description'],
                image=rim_data['image']
            )
            for variant_data in rim_data['variants']:
                RimVariant.objects.create(
                    model=rim_model,
                    **variant_data
                )
        self.stdout.write(self.style.SUCCESS('Successfully seeded rim data.')) 