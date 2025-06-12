from django.urls import path
from . import views

app_name = 'tyres'

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('tyre/<int:tyre_id>/', views.tyre_detail, name='tyre_detail'),
    path('rim/<int:rim_id>/', views.rim_detail, name='rim_detail'),
    path('rims/', views.rim_list, name='rim_list'),
    path('faq/', views.faq, name='faq'),
    
    # Избранное
    path('favourite/add/<int:variant_id>/', views.add_to_favourites, name='add_to_favourites'),
    path('favourite/remove/<int:variant_id>/', views.remove_from_favourites, name='remove_from_favourites'),
    path('favourite/rim/add/<int:rim_variant_id>/', views.add_rim_to_favourites, name='add_rim_to_favourites'),
    path('favourite/rim/remove/<int:rim_variant_id>/', views.remove_rim_from_favourites, name='remove_rim_from_favourites'),
    path('favourites/', views.favourites, name='favourites'),
    
    # Админ-панель
    path('admin/tyres/', views.admin_tyres, name='admin_tyres'),
    path('admin/rims/', views.admin_rims, name='admin_rims'),
    path('admin/categories/', views.admin_categories, name='admin_categories'),
    
    # CRUD операции для шин
    path('admin/tyre/add/', views.admin_tyre_add, name='add_tyre'),
    path('admin/tyre/<int:tyre_id>/edit/', views.admin_tyre_edit, name='edit_tyre'),
    path('admin/tyre/<int:tyre_id>/delete/', views.admin_tyre_delete, name='delete_tyre'),
    
    # CRUD операции для дисков
    path('admin/rim/add/', views.admin_rim_add, name='add_rim'),
    path('admin/rim/<int:rim_id>/edit/', views.admin_rim_edit, name='edit_rim'),
    path('admin/rim/<int:rim_id>/delete/', views.admin_rim_delete, name='delete_rim'),
] 