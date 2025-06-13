#!/usr/bin/env python
"""
Скрипт для проверки URL-маршрутов Django
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyre_trust.settings')
django.setup()

from django.urls import get_resolver

def print_urls(patterns, base='', indent=0):
    """
    Рекурсивно выводит все URL-маршруты
    """
    for pattern in patterns:
        if hasattr(pattern, 'pattern'):
            # Это URLPattern
            if hasattr(pattern, 'name') and pattern.name:
                print(f"{' ' * indent}{base}{pattern.pattern} - {pattern.name}")
            else:
                print(f"{' ' * indent}{base}{pattern.pattern}")
        elif hasattr(pattern, 'url_patterns'):
            # Это URLResolver (включенный URL-конфиг)
            if hasattr(pattern, 'namespace') and pattern.namespace:
                print(f"\n{' ' * indent}[Namespace: {pattern.namespace}]")
            if hasattr(pattern, 'app_name') and pattern.app_name:
                print(f"{' ' * indent}[App: {pattern.app_name}]")
            print(f"{' ' * indent}{base}{pattern.pattern}")
            print_urls(pattern.url_patterns, '', indent + 2)

if __name__ == '__main__':
    resolver = get_resolver()
    print("\nURL-маршруты проекта:")
    print("=====================")
    print_urls(resolver.url_patterns)
    
    print("\nПроверка URL-маршрутов для приложения accounts:")
    print("=========================================")
    for pattern in resolver.url_patterns:
        if hasattr(pattern, 'pattern') and 'accounts' in str(pattern.pattern):
            print(f"Найден URL-маршрут: {pattern.pattern}")
            if hasattr(pattern, 'url_patterns'):
                print("Дочерние URL-маршруты:")
                for child in pattern.url_patterns:
                    if hasattr(child, 'name') and child.name:
                        print(f" - {child.pattern} - {child.name}")
                    else:
                        print(f" - {child.pattern}")
    
    # Проверяем наличие URL для admin-panel
    print("\nПоиск URL-маршрута для admin-panel:")
    print("================================")
    found = False
    for pattern in resolver.url_patterns:
        if hasattr(pattern, 'url_patterns'):
            for child in pattern.url_patterns:
                if hasattr(child, 'name') and child.name == 'admin_panel':
                    found = True
                    print(f"Найден URL для admin_panel: {pattern.pattern}{child.pattern}")
                    print(f"Namespace: {pattern.namespace if hasattr(pattern, 'namespace') else 'None'}")
                    print(f"App name: {pattern.app_name if hasattr(pattern, 'app_name') else 'None'}")
                    break
    
    if not found:
        print("URL для admin_panel не найден!") 