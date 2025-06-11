from django.core.management.base import BaseCommand
from tyres.models import TyreModel, TyreVariant

class Command(BaseCommand):
    help = 'Seeds the database with ONLY existing tyres (16), matching available images.'

    def handle(self, *args, **kwargs):
        tyres_data = [
            {
                'brand': 'Michelin',
                'name': 'X-Ice North 4',
                'description': 'Зимняя шина с отличным сцеплением на льду и снегу. Максимальная безопасность в суровых условиях.',
                'image': 'tyres/michelinx-icenorth4.jpg',
                'variants': [
                    {'width': 205, 'profile': 55, 'radius': 16, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': 7500, 'stock': 10},
                    {'width': 215, 'profile': 60, 'radius': 17, 'season': 'winter', 'studded': False, 'speed_index': 'H', 'price': 8200, 'stock': 5},
                ]
            },
            {
                'brand': 'Nokian',
                'name': 'Nordman SX2',
                'description': 'Летняя шина для городских дорог. Отличается долговечностью и низким уровнем шума.',
                'image': 'tyres/NokianNordmanSX2.jpg',
                'variants': [
                    {'width': 195, 'profile': 65, 'radius': 15, 'season': 'summer', 'studded': False, 'speed_index': 'T', 'price': 6100, 'stock': 10},
                ]
            },
            {
                'brand': 'Nokian',
                'name': 'Hakkapeliitta 10',
                'description': 'Финская зимняя шина для суровой зимы. Отличное сцепление на льду и снегу.',
                'image': 'tyres/nokianhakkapelita10.jpg',
                'variants': [
                    {'width': 205, 'profile': 55, 'radius': 16, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': 7900, 'stock': 6},
                ]
            },
            {
                'brand': 'Michelin',
                'name': 'Pilot Sport 4',
                'description': 'Летняя шина для динамичной езды. Отличное сцепление и управляемость.',
                'image': 'tyres/MichelinPilotSport4.jpg',
                'variants': [
                    {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'W', 'price': 9800, 'stock': 7},
                ]
            },
            {
                'brand': 'Michelin',
                'name': 'Energy Saver',
                'description': 'Экономичная летняя шина для городских автомобилей. Снижает расход топлива.',
                'image': 'tyres/MichelinEnergySaver.jpg',
                'variants': [
                    {'width': 195, 'profile': 65, 'radius': 15, 'season': 'summer', 'studded': False, 'speed_index': 'T', 'price': 5700, 'stock': 11},
                ]
            },
            {
                'brand': 'Michelin',
                'name': 'CrossClimate',
                'description': 'Всесезонная шина с отличным сцеплением на сухой и мокрой дороге.',
                'image': 'tyres/michelincrossclimate.jpg',
                'variants': [
                    {'width': 205, 'profile': 60, 'radius': 16, 'season': 'all_season', 'studded': False, 'speed_index': 'H', 'price': 8700, 'stock': 4},
                ]
            },
            {
                'brand': 'Goodyear',
                'name': 'Vector 4Seasons Gen-3',
                'description': 'Всесезонная шина для любых погодных условий. Отличная управляемость круглый год.',
                'image': 'tyres/GoodyearVector4SeasonsGen-3.jpg',
                'variants': [
                    {'width': 215, 'profile': 55, 'radius': 17, 'season': 'all_season', 'studded': False, 'speed_index': 'V', 'price': 9200, 'stock': 6},
                ]
            },
            {
                'brand': 'Goodyear',
                'name': 'UltraGrip Ice 2',
                'description': 'Зимняя нешипованная шина для легковых авто. Отличное сцепление на льду.',
                'image': 'tyres/goodyearultragripice2.jpg',
                'variants': [
                    {'width': 205, 'profile': 60, 'radius': 16, 'season': 'winter', 'studded': False, 'speed_index': 'H', 'price': 7300, 'stock': 5},
                ]
            },
            {
                'brand': 'Goodyear',
                'name': 'EfficientGrip Performance',
                'description': 'Летняя шина для мокрой дороги. Короткий тормозной путь и низкий расход топлива.',
                'image': 'tyres/GoodyearEfficientGripPerformance.jpg',
                'variants': [
                    {'width': 205, 'profile': 55, 'radius': 16, 'season': 'summer', 'studded': False, 'speed_index': 'V', 'price': 7100, 'stock': 9},
                ]
            },
            {
                'brand': 'Gislaved',
                'name': 'Nord Frost 200',
                'description': 'Надежная зимняя шина для России. Отличное сцепление на снегу и льду.',
                'image': 'tyres/gislavednordfrost200.jpg',
                'variants': [
                    {'width': 215, 'profile': 55, 'radius': 16, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': 7900, 'stock': 6},
                ]
            },
            {
                'brand': 'Continental',
                'name': 'IceContact 3',
                'description': 'Современная зимняя шина для суровых условий. Максимальное сцепление на льду.',
                'image': 'tyres/continentalicecontact3.jpg',
                'variants': [
                    {'width': 205, 'profile': 60, 'radius': 16, 'season': 'winter', 'studded': False, 'speed_index': 'H', 'price': 8100, 'stock': 7},
                ]
            },
            {
                'brand': 'Continental',
                'name': 'EcoContact 6',
                'description': 'Экономичная летняя шина. Снижает расход топлива и увеличивает пробег.',
                'image': 'tyres/ContinentalEcoContact6.jpg',
                'variants': [
                    {'width': 205, 'profile': 55, 'radius': 16, 'season': 'summer', 'studded': False, 'speed_index': 'V', 'price': 7200, 'stock': 8},
                ]
            },
            {
                'brand': 'Continental',
                'name': 'AllSeasonContact',
                'description': 'Всесезонная шина для любых погодных условий. Отличная управляемость и комфорт.',
                'image': 'tyres/continentalallseasonscontact.jpg',
                'variants': [
                    {'width': 205, 'profile': 60, 'radius': 16, 'season': 'all_season', 'studded': False, 'speed_index': 'H', 'price': 8700, 'stock': 4},
                ]
            },
            {
                'brand': 'Bridgestone',
                'name': 'Turanza T005',
                'description': 'Летняя шина для комфорта и безопасности. Отличная управляемость на мокрой дороге.',
                'image': 'tyres/BridgestoneTuranzaT005.jpg',
                'variants': [
                    {'width': 215, 'profile': 60, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'W', 'price': 8300, 'stock': 5},
                ]
            },
            {
                'brand': 'Bridgestone',
                'name': 'Blizzak VRX3',
                'description': 'Японская зимняя шина для города и трассы. Отличное сцепление на льду.',
                'image': 'tyres/bridgestoneblizzakvrx3.jpg',
                'variants': [
                    {'width': 215, 'profile': 55, 'radius': 17, 'season': 'winter', 'studded': False, 'speed_index': 'H', 'price': 13000, 'stock': 18},
                ]
            },
            {
                'brand': 'Toyo',
                'name': 'Proxes R888R',
                'description': 'Полуслик для трека и быстрой езды. Максимальное сцепление на сухом покрытии.',
                'image': 'tyres/toyoproxesr888r.jpg',
                'variants': [
                    {'width': 235, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': 13000, 'stock': 25},
                ]
            },
        ]

        for tyre_data in tyres_data:
            tyre_model = TyreModel.objects.create(
                brand=tyre_data['brand'],
                name=tyre_data['name'],
                description=tyre_data['description'],
                image=tyre_data['image']
            )
            for variant_data in tyre_data['variants']:
                TyreVariant.objects.create(
                    model=tyre_model,
                    **variant_data
                ) 