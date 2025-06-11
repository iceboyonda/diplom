import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyre_trust.settings')
django.setup()

from tyres.models import TyreModel, TyreVariant
from decimal import Decimal

# Очищаем существующие шины
print(f"Удаление существующих моделей шин ({TyreModel.objects.count()} шт.)...")
TyreModel.objects.all().delete()
print(f"Осталось моделей шин после удаления: {TyreModel.objects.count()} шт.")

# Список популярных моделей шин с их вариациями
tyres_data = [
    {
        'brand': 'Michelin',
        'name': 'Pilot Sport 4',
        'description': 'Высокопроизводительные спортивные шины с отличной управляемостью и сцеплением на сухой и мокрой дороге. Обеспечивают превосходную устойчивость и комфортное вождение.',
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'summer', 'studded': False, 'speed_index': 'V', 'price': Decimal('7500.00'), 'stock': 15},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'W', 'price': Decimal('9200.00'), 'stock': 12},
            {'width': 245, 'profile': 40, 'radius': 18, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('12400.00'), 'stock': 8},
            {'width': 255, 'profile': 35, 'radius': 19, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('15800.00'), 'stock': 6}
        ]
    },
    {
        'brand': 'Continental',
        'name': 'PremiumContact 6',
        'description': 'Превосходная управляемость, короткий тормозной путь и низкий уровень шума. Идеальный выбор для водителей, ценящих комфорт и безопасность.',
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'summer', 'studded': False, 'speed_index': 'H', 'price': Decimal('5600.00'), 'stock': 18},
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'summer', 'studded': False, 'speed_index': 'V', 'price': Decimal('6800.00'), 'stock': 20},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('8900.00'), 'stock': 14},
            {'width': 245, 'profile': 40, 'radius': 18, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('11200.00'), 'stock': 10}
        ]
    },
    {
        'brand': 'Pirelli',
        'name': 'P Zero',
        'description': 'Спортивные шины премиум-класса с улучшенной управляемостью и характеристиками на высокой скорости. Разработаны для спортивных и премиальных автомобилей.',
        'variants': [
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('10500.00'), 'stock': 12},
            {'width': 245, 'profile': 40, 'radius': 18, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('13800.00'), 'stock': 8},
            {'width': 255, 'profile': 35, 'radius': 19, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('16500.00'), 'stock': 6},
            {'width': 275, 'profile': 30, 'radius': 20, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('22000.00'), 'stock': 4}
        ]
    },
    {
        'brand': 'Bridgestone',
        'name': 'Blizzak WS90',
        'description': 'Зимние шины с превосходным сцеплением на снегу и льду. Улучшенная технология резиновой смеси обеспечивает отличную маневренность в суровых зимних условиях.',
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'winter', 'studded': False, 'speed_index': 'T', 'price': Decimal('6200.00'), 'stock': 22},
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'winter', 'studded': False, 'speed_index': 'T', 'price': Decimal('7500.00'), 'stock': 18},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'winter', 'studded': False, 'speed_index': 'T', 'price': Decimal('9800.00'), 'stock': 14},
            {'width': 235, 'profile': 40, 'radius': 18, 'season': 'winter', 'studded': False, 'speed_index': 'T', 'price': Decimal('12400.00'), 'stock': 10}
        ]
    },
    {
        'brand': 'Nokian',
        'name': 'Hakkapeliitta 10',
        'description': 'Лучшие зимние шипованные шины для суровых зимних условий. Отличное сцепление на льду и снегу благодаря инновационному расположению шипов.',
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('7800.00'), 'stock': 24},
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('8900.00'), 'stock': 20},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('11200.00'), 'stock': 16},
            {'width': 235, 'profile': 40, 'radius': 18, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('14500.00'), 'stock': 12}
        ]
    },
    {
        'brand': 'Goodyear',
        'name': 'Vector 4Seasons Gen-3',
        'description': 'Всесезонные шины с превосходными характеристиками в любое время года. Оптимальное решение для регионов с мягким климатом.',
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'all_season', 'studded': False, 'speed_index': 'V', 'price': Decimal('5900.00'), 'stock': 16},
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'all_season', 'studded': False, 'speed_index': 'V', 'price': Decimal('6800.00'), 'stock': 14},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'all_season', 'studded': False, 'speed_index': 'W', 'price': Decimal('8500.00'), 'stock': 12},
            {'width': 235, 'profile': 40, 'radius': 18, 'season': 'all_season', 'studded': False, 'speed_index': 'W', 'price': Decimal('10800.00'), 'stock': 8}
        ]
    },
    {
        'brand': 'Hankook',
        'name': 'Ventus S1 Evo3',
        'description': 'Спортивные летние шины с превосходными характеристиками на сухой дороге. Улучшенный состав резиновой смеси для увеличения срока службы.',
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'summer', 'studded': False, 'speed_index': 'V', 'price': Decimal('5200.00'), 'stock': 18},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'W', 'price': Decimal('6500.00'), 'stock': 14},
            {'width': 245, 'profile': 40, 'radius': 18, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('8200.00'), 'stock': 10}
        ]
    },
    {
        'brand': 'Yokohama',
        'name': 'BluEarth-GT AE51',
        'description': 'Экологичные летние шины с низким сопротивлением качению. Отличная топливная экономичность и повышенный комфорт.',
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'summer', 'studded': False, 'speed_index': 'H', 'price': Decimal('4800.00'), 'stock': 22},
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'summer', 'studded': False, 'speed_index': 'V', 'price': Decimal('5600.00'), 'stock': 18},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'W', 'price': Decimal('7200.00'), 'stock': 14}
        ]
    },
    {
        'brand': 'Toyo',
        'name': 'Observe GSi-6',
        'description': 'Зимние шины с отличным сцеплением на снегу и льду. Усиленная боковина для защиты от ударов и повреждений.',
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'winter', 'studded': False, 'speed_index': 'T', 'price': Decimal('5800.00'), 'stock': 20},
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'winter', 'studded': False, 'speed_index': 'T', 'price': Decimal('6900.00'), 'stock': 16},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'winter', 'studded': False, 'speed_index': 'T', 'price': Decimal('8500.00'), 'stock': 12}
        ]
    },
    {
        'brand': 'Dunlop',
        'name': 'SP Sport Maxx RT2',
        'description': 'Спортивные шины с улучшенной управляемостью на высокой скорости. Короткий тормозной путь и хорошая стойкость к аквапланированию.',
        'variants': [
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('7800.00'), 'stock': 14},
            {'width': 245, 'profile': 40, 'radius': 18, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('9500.00'), 'stock': 10},
            {'width': 255, 'profile': 35, 'radius': 19, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('12200.00'), 'stock': 8}
        ]
    },
    {
        'brand': 'Kumho',
        'name': 'Ecsta PS71',
        'description': 'Доступные спортивные шины с хорошими ходовыми характеристиками. Оптимальное соотношение цены и качества.',
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'summer', 'studded': False, 'speed_index': 'W', 'price': Decimal('4500.00'), 'stock': 20},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'W', 'price': Decimal('5800.00'), 'stock': 16},
            {'width': 245, 'profile': 40, 'radius': 18, 'season': 'summer', 'studded': False, 'speed_index': 'W', 'price': Decimal('7200.00'), 'stock': 12}
        ]
    },
    {
        'brand': 'Gislaved',
        'name': 'Nord Frost 200',
        'description': 'Надежные зимние шипованные шины для суровых зимних условий. Хорошее соотношение цены и качества.',
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('5200.00'), 'stock': 22},
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('6300.00'), 'stock': 18},
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('7800.00'), 'stock': 14}
        ]
    }
]

# Добавляем шины в базу данных
for tyre_data in tyres_data:
    tyre = TyreModel.objects.create(
        brand=tyre_data['brand'],
        name=tyre_data['name'],
        description=tyre_data['description']
    )
    print(f"Добавлена модель шин: {tyre.brand} {tyre.name}")
    
    for variant_data in tyre_data['variants']:
        TyreVariant.objects.create(
            model=tyre,
            **variant_data
        )

print("Шины успешно добавлены в базу данных!")
print(f"Всего моделей шин в базе: {TyreModel.objects.count()} шт.") 