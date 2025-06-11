import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyre_trust.settings')
django.setup()

from tyres.models import TyreModel, TyreVariant, RimModel, RimVariant
from decimal import Decimal

# Очищаем существующие данные
print("Удаление существующих данных...")
TyreModel.objects.all().delete()
RimModel.objects.all().delete()

# Список шин с соответствующими фотографиями
tyres_data = [
    {
        'brand': 'Michelin',
        'name': 'X-Ice North 4',
        'description': 'Флагманская зимняя шипованная шина Michelin для суровых северных условий. Оснащена инновационной системой шипования Michelin EvoGrip с 250 шипами особой формы, обеспечивающими максимальное сцепление на льду. Уникальный состав резиновой смеси с добавлением подсолнечного масла сохраняет эластичность при экстремально низких температурах. Направленный рисунок протектора эффективно отводит воду и снежную шугу.',
        'image': 'tyres/michelinx-icenorth4.jpg',
        'release_year': 2020,
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('7500.00'), 'stock': 10},
        ]
    },
    {
        'brand': 'Nokian',
        'name': 'Hakkapeliitta 10',
        'description': 'Премиальная зимняя шипованная шина от финского производителя. Оснащена двухфланцевыми шипами с уникальной технологией Dynamic Grip, которая адаптируется к дорожным условиям. Экологичная резиновая смесь Green Elasto Proof сохраняет эластичность при температурах до -45°C. Ламели Double Block с технологией Pump Sipes активно удаляют воду и снежную кашу из пятна контакта.',
        'image': 'tyres/nokianhakkapelita10.jpg',
        'release_year': 2021,
        'variants': [
            {'width': 215, 'profile': 55, 'radius': 17, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('8200.00'), 'stock': 8},
        ]
    },
    {
        'brand': 'Nokian',
        'name': 'Nordman SX2',
        'description': 'Летняя шина среднего класса от Nokian с отличным соотношением цена/качество. Асимметричный рисунок протектора с четырьмя широкими продольными канавками обеспечивает надежную защиту от аквапланирования. Специальная резиновая смесь с добавлением силики гарантирует хорошее сцепление на мокрой дороге и низкое сопротивление качению. Усиленная конструкция боковины повышает устойчивость к повреждениям.',
        'image': 'tyres/NokianNordmanSX2.jpg',
        'release_year': 2019,
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'summer', 'studded': False, 'speed_index': 'H', 'price': Decimal('4200.00'), 'stock': 15},
        ]
    },
    {
        'brand': 'Toyo',
        'name': 'Proxes R888R',
        'description': 'Экстремально спортивная полусликовая шина для трека и дрифта. Имеет жесткую конструкцию каркаса и специальный состав резиновой смеси для максимального сцепления в сухих условиях. Уникальный направленный рисунок протектора с минимальным количеством канавок обеспечивает максимальную площадь контакта с дорогой. Не рекомендуется для повседневного использования на обычных дорогах.',
        'image': 'tyres/toyoproxesr888r.jpg',
        'release_year': 2018,
        'variants': [
            {'width': 245, 'profile': 40, 'radius': 18, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('12500.00'), 'stock': 6},
        ]
    },
    {
        'brand': 'Bridgestone',
        'name': 'Blizzak VRX3',
        'description': 'Инновационная нешипованная зимняя шина с технологией Multi-Cell Compound. Микропористая структура протектора с множеством микроскопических ячеек эффективно впитывает воду с поверхности льда, значительно улучшая сцепление. Асимметричный рисунок протектора с технологией направленных 3D-ламелей обеспечивает стабильное поведение на снегу и мокрой дороге.',
        'image': 'tyres/bridgestoneblizzakvrx3.jpg',
        'release_year': 2022,
        'variants': [
            {'width': 215, 'profile': 55, 'radius': 17, 'season': 'winter', 'studded': False, 'speed_index': 'T', 'price': Decimal('7800.00'), 'stock': 12},
        ]
    },
    {
        'brand': 'Bridgestone',
        'name': 'Turanza T005',
        'description': 'Премиальная летняя шина для комфортного вождения. Использует инновационную технологию NanoPro-Tech™ для улучшения сцепления на мокрой дороге. Оптимизированный рисунок протектора с технологией Quick Response Shoulder обеспечивает точную управляемость и короткий тормозной путь. Специальная конструкция каркаса с технологией Noise Reducing Pattern значительно снижает шум при движении.',
        'image': 'tyres/BridgestoneTuranzaT005.jpg',
        'release_year': 2020,
        'variants': [
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'W', 'price': Decimal('8900.00'), 'stock': 8},
        ]
    },
    {
        'brand': 'Continental',
        'name': 'AllSeasonContact',
        'description': 'Универсальная всесезонная шина с технологией Traction Silica Compound. Адаптивный рисунок протектора с технологией Weather Activated Polymers обеспечивает стабильные характеристики в любую погоду. Многочисленные ламели с технологией 3D Grip Sipes улучшают сцепление на мокрой дороге и снегу. Идеальный выбор для регионов с мягкой зимой.',
        'image': 'tyres/continentalallseasonscontact.jpg',
        'release_year': 2021,
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'all_season', 'studded': False, 'speed_index': 'V', 'price': Decimal('7200.00'), 'stock': 10},
        ]
    },
    {
        'brand': 'Continental',
        'name': 'EcoContact 6',
        'description': 'Экологичная летняя шина с низким сопротивлением качению. Использует инновационную технологию Green Chili 2.0 для снижения расхода топлива без потери сцепных свойств. Оптимизированный асимметричный рисунок протектора с технологией Aqua Grooves обеспечивает отличную защиту от аквапланирования. Усиленная боковина с технологией ContiSilent снижает уровень шума.',
        'image': 'tyres/ContinentalEcoContact6.jpg',
        'release_year': 2019,
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'summer', 'studded': False, 'speed_index': 'V', 'price': Decimal('6800.00'), 'stock': 14},
        ]
    },
    {
        'brand': 'Continental',
        'name': 'IceContact 3',
        'description': 'Премиальная зимняя шипованная шина с технологией IceGrip. Оснащена инновационными шипами с алмазным напылением, обеспечивающими максимальное сцепление на льду. Уникальная конструкция шипов с технологией Secure Winter Contact снижает их выпадение. Специальный состав резиновой смеси Arctic Plus сохраняет эластичность при экстремально низких температурах.',
        'image': 'tyres/continentalicecontact3.jpg',
        'release_year': 2020,
        'variants': [
            {'width': 215, 'profile': 55, 'radius': 17, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('8500.00'), 'stock': 8},
        ]
    },
    {
        'brand': 'Gislaved',
        'name': 'Nord Frost 200',
        'description': 'Надежная зимняя шипованная шина среднего класса. Оптимизированный рисунок протектора с технологией Snow Grip обеспечивает уверенное поведение на заснеженных дорогах. Усиленная конструкция шипов с технологией TwinLock гарантирует их надежную фиксацию. Специальная резиновая смесь с добавлением натурального каучука сохраняет эластичность в мороз.',
        'image': 'tyres/gislavednordfrost200.jpg',
        'release_year': 2018,
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'winter', 'studded': True, 'speed_index': 'T', 'price': Decimal('4800.00'), 'stock': 16},
        ]
    },
    {
        'brand': 'Goodyear',
        'name': 'EfficientGrip Performance',
        'description': 'Высокотехнологичная летняя шина с технологией WearControl. Инновационный состав резиновой смеси с полимерами последнего поколения обеспечивает длительный срок службы. Оптимизированный рисунок протектора с технологией ActiveBraking увеличивает площадь контакта при торможении. Специальная конструкция блоков протектора снижает уровень шума.',
        'image': 'tyres/GoodyearEfficientGripPerformance.jpg',
        'release_year': 2021,
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'summer', 'studded': False, 'speed_index': 'V', 'price': Decimal('6500.00'), 'stock': 12},
        ]
    },
    {
        'brand': 'Goodyear',
        'name': 'UltraGrip Ice 2',
        'description': 'Нешипованная зимняя шина премиум-класса с технологией ActiveGrip. Уникальный состав резиновой смеси с добавлением силики и рапсового масла обеспечивает отличное сцепление на льду. Направленный рисунок протектора с технологией SnowProtect эффективно отводит снег и слякоть. Многочисленные ламели с технологией 3D-BIS улучшают управляемость на зимней дороге.',
        'image': 'tyres/goodyearultragripice2.jpg',
        'release_year': 2019,
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'winter', 'studded': False, 'speed_index': 'T', 'price': Decimal('7200.00'), 'stock': 10},
        ]
    },
    {
        'brand': 'Goodyear',
        'name': 'Vector 4Seasons Gen-3',
        'description': 'Инновационная всесезонная шина с технологией SmartTRED Climate Adapt. Адаптивный рисунок протектора меняет характеристики в зависимости от погодных условий. Специальная резиновая смесь с технологией Weather Reactive обеспечивает стабильное сцепление в любое время года. Усиленная конструкция каркаса повышает устойчивость к деформациям.',
        'image': 'tyres/GoodyearVector4SeasonsGen-3.jpg',
        'release_year': 2022,
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'all_season', 'studded': False, 'speed_index': 'V', 'price': Decimal('7800.00'), 'stock': 8},
        ]
    },
    {
        'brand': 'Michelin',
        'name': 'CrossClimate',
        'description': 'Революционная всесезонная шина с зимней сертификацией 3PMSF. Уникальный V-образный рисунок протектора с технологией Thermal Adaptive обеспечивает отличные характеристики в любую погоду. Инновационная резиновая смесь с технологией Dynamic Response адаптируется к температуре. Усиленная конструкция боковины с технологией MaxTouch Construction равномерно распределяет нагрузки.',
        'image': 'tyres/michelincrossclimate.jpg',
        'release_year': 2021,
        'variants': [
            {'width': 205, 'profile': 55, 'radius': 16, 'season': 'all_season', 'studded': False, 'speed_index': 'V', 'price': Decimal('8900.00'), 'stock': 6},
        ]
    },
    {
        'brand': 'Michelin',
        'name': 'Energy Saver',
        'description': 'Экономичная летняя шина с технологией EnergyTM. Специальный состав резиновой смеси с силикой последнего поколения снижает сопротивление качению на 20%. Оптимизированный рисунок протектора с технологией Green Power Compound уменьшает расход топлива. Усиленная конструкция каркаса с технологией MaxTouch Construction увеличивает срок службы.',
        'image': 'tyres/MichelinEnergySaver.jpg',
        'release_year': 2020,
        'variants': [
            {'width': 195, 'profile': 65, 'radius': 15, 'season': 'summer', 'studded': False, 'speed_index': 'H', 'price': Decimal('5900.00'), 'stock': 14},
        ]
    },
    {
        'brand': 'Michelin',
        'name': 'Pilot Sport 4',
        'description': 'Спортивная летняя шина премиум-класса с технологией Dynamic Response. Асимметричный рисунок протектора с жесткими внешними блоками обеспечивает точную управляемость на высоких скоростях. Инновационная резиновая смесь с функциональными эластомерами гарантирует максимальное сцепление на сухой и мокрой дороге. Усиленная конструкция каркаса с арамидными нитями повышает стабильность.',
        'image': 'tyres/MichelinPilotSport4.jpg',
        'release_year': 2021,
        'variants': [
            {'width': 225, 'profile': 45, 'radius': 17, 'season': 'summer', 'studded': False, 'speed_index': 'Y', 'price': Decimal('11500.00'), 'stock': 6},
        ]
    },
]

# Список дисков с соответствующими фотографиями
rims_data = [
    {
        'brand': 'BBS',
        'name': 'CH-R',
        'description': 'Легендарные немецкие диски BBS CH-R, изготовленные из высокопрочного алюминиевого сплава методом ковки. Благодаря Y-образному дизайну спиц и оптимизированной геометрии, диски обладают превосходными показателями жесткости при минимальном весе. Идеально подходят для спортивных и премиальных автомобилей, обеспечивая не только великолепный внешний вид, но и улучшенные динамические характеристики.',
        'image': 'rims/bbschr.jpg',
        'release_year': 2019,
        'variants': [
            {'diameter': 18.0, 'width': 8.0, 'bolt_pattern': '5x120', 'offset': '35', 'dia': '72.6', 'color': 'серебристый', 'material': 'кованый алюминиевый сплав', 'price': Decimal('21250.00'), 'stock': 5},
        ]
    },
    {
        'brand': 'Vossen',
        'name': 'HF-3',
        'description': 'Современные диски Vossen HF-3 с изящным дизайном в стиле "турбовеер". Изготовлены из авиационного алюминиевого сплава 6061-T6 с применением технологии гибридной ковки, что обеспечивает оптимальное соотношение прочности и веса. Многоступенчатая система контроля качества и индивидуальная проверка каждого диска гарантируют безупречное качество продукта.',
        'image': 'rims/vossenhf3.jpg',
        'release_year': 2021,
        'variants': [
            {'diameter': 19.0, 'width': 8.5, 'bolt_pattern': '5x112', 'offset': '45', 'dia': '66.6', 'color': 'серебристый', 'material': 'гибридный алюминиевый сплав', 'price': Decimal('16250.00'), 'stock': 4},
        ]
    },
    {
        'brand': 'Rays',
        'name': 'TE37',
        'description': 'Культовые японские диски Rays TE37 с шестиспицевым дизайном, ставшие легендой в мире автоспорта. Производятся из специального алюминиевого сплава MAT-DURA с применением технологии цельной ковки, что обеспечивает исключительную прочность при минимальном весе. Каждый диск проходит рентгеновский контроль качества и имеет индивидуальный серийный номер.',
        'image': 'rims/TE37.png',
        'release_year': 2018,
        'variants': [
            {'diameter': 18.0, 'width': 9.5, 'bolt_pattern': '5x114.3', 'offset': '22', 'dia': '73.1', 'color': 'бронзовый', 'material': 'кованый алюминиевый сплав MAT-DURA', 'price': Decimal('23750.00'), 'stock': 3},
        ]
    },
    {
        'brand': 'Work',
        'name': 'Emotion CR Kai',
        'description': 'Премиальные японские диски Work Emotion CR Kai с агрессивным многоспицевым дизайном. Изготовлены из высокопрочного алюминиевого сплава T6-6061 методом ковки с последующей механической обработкой. Трехсекционная конструкция позволяет создавать уникальные цветовые комбинации. Специальное покрытие Super Hard Clear защищает поверхность от коррозии и механических повреждений.',
        'image': 'rims/worksrkai.jpg',
        'release_year': 2020,
        'variants': [
            {'diameter': 18.0, 'width': 9.5, 'bolt_pattern': '5x114.3', 'offset': '30', 'dia': '73.1', 'color': 'белый', 'material': 'кованый алюминиевый сплав T6-6061', 'price': Decimal('78000.00'), 'stock': 6},
        ]
    },
    {
        'brand': 'OZ Racing',
        'name': 'Ultraleggera',
        'description': 'Итальянские гоночные диски OZ Racing Ultraleggera, разработанные с использованием технологий Formula 1. Изготовлены из легкого алюминиевого сплава с применением технологии ротационной ковки. Специальная конструкция спиц и оптимизированная геометрия обеспечивают максимальную прочность при весе всего 8 кг. Каждый диск проходит рентгенографический контроль качества.',
        'image': 'rims/ozracingultraleggera.jpg',
        'release_year': 2021,
        'variants': [
            {'diameter': 17.0, 'width': 8.0, 'bolt_pattern': '5x112', 'offset': '35', 'dia': '75.0', 'color': 'черный', 'material': 'кованый алюминиевый сплав', 'price': Decimal('18000.00'), 'stock': 8},
        ]
    },
    {
        'brand': 'Enkei',
        'name': 'RPF1',
        'description': 'Легендарные гоночные диски Enkei RPF1, созданные с применением эксклюзивной технологии MAT (Most Advanced Technology). Изготовлены из специального алюминиевого сплава методом литья под давлением с последующей термической обработкой. Обладают отличным соотношением прочности и веса благодаря оптимизированной конструкции спиц. Широко используются в кольцевых гонках и дрифте.',
        'image': 'rims/enkeirpf1.jpg',
        'release_year': 2019,
        'variants': [
            {'diameter': 17.0, 'width': 8.0, 'bolt_pattern': '5x114.3', 'offset': '35', 'dia': '73.1', 'color': 'серебристый', 'material': 'литой алюминиевый сплав', 'price': Decimal('11250.00'), 'stock': 10},
        ]
    },
    {
        'brand': 'DOTZ',
        'name': 'Hanzo',
        'description': 'Стильные европейские диски DOTZ Hanzo, разработанные специально для современных городских автомобилей. Изготовлены из высококачественного алюминиевого сплава методом литья под низким давлением с применением технологии Flow Forming. Элегантный дизайн с десятью тонкими спицами подчеркивает динамичный характер автомобиля. Имеют сертификаты TUV и JWL.',
        'image': 'rims/dotzhanzo.jpg',
        'release_year': 2020,
        'variants': [
            {'diameter': 18.0, 'width': 8.0, 'bolt_pattern': '5x112', 'offset': '45', 'dia': '66.6', 'color': 'черный', 'material': 'литой алюминиевый сплав', 'price': Decimal('9500.00'), 'stock': 12},
        ]
    },
    {
        'brand': 'Rotiform',
        'name': 'LAS-R',
        'description': 'Премиальные диски Rotiform LAS-R из новой линейки бренда. Изготовлены из фирменного алюминиевого сплава методом многоступенчатой ковки с применением технологии Anti-Chipping. Ультрасовременный дизайн с асимметричными спицами создает эффект постоянного движения. Многослойное покрытие Diamond Cut обеспечивает долговечный блеск и защиту от коррозии.',
        'image': 'rims/lasr.jpg',
        'release_year': 2022,
        'variants': [
            {'diameter': 19.0, 'width': 8.5, 'bolt_pattern': '5x114.3', 'offset': '40', 'dia': '73.1', 'color': 'серебристый', 'material': 'кованый алюминиевый сплав A-MAT', 'price': Decimal('20500.00'), 'stock': 4},
        ]
    },
    {
        'brand': 'Rial',
        'name': 'Lucca',
        'description': 'Элегантные немецкие диски Rial Lucca с классическим мультиспицевым дизайном. Изготовлены из высококачественного алюминиевого сплава методом литья под низким давлением. Специальная технология покраски Sterling Silver обеспечивает стойкость к механическим повреждениям и агрессивным средам. Имеют европейские сертификаты качества ECE и TUV.',
        'image': 'rims/riallucca.jpg',
        'release_year': 2021,
        'variants': [
            {'diameter': 17.0, 'width': 7.5, 'bolt_pattern': '5x112', 'offset': '45', 'dia': '66.6', 'color': 'серебристый', 'material': 'литой алюминиевый сплав', 'price': Decimal('8750.00'), 'stock': 15},
        ]
    },
]

# Добавляем шины в базу данных
print("\nДобавление шин в базу данных...")
for tyre_data in tyres_data:
    variants = tyre_data.pop('variants')
    tyre_model = TyreModel.objects.create(**tyre_data)
    for variant in variants:
        TyreVariant.objects.create(model=tyre_model, **variant)
    print(f"Добавлена модель шин: {tyre_model.brand} {tyre_model.name}")

# Добавляем диски в базу данных
print("\nДобавление дисков в базу данных...")
for rim_data in rims_data:
    variants = rim_data.pop('variants')
    rim_model = RimModel.objects.create(**rim_data)
    for variant in variants:
        RimVariant.objects.create(model=rim_model, **variant)
    print(f"Добавлена модель дисков: {rim_model.brand} {rim_model.name}")

print("\nОбновление базы данных завершено!")
print(f"Всего моделей шин в базе: {TyreModel.objects.count()} шт.")
print(f"Всего моделей дисков в базе: {RimModel.objects.count()} шт.") 