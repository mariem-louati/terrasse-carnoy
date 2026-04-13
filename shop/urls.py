from django.urls import path
from . import views

urlpatterns = [
    # 🏠 Accueil
    path('', views.product_list, name='product_list'),

    # 📂 Catégories
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),

    # 🛒 Panier
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('debug/', views.debug_images, name='debug_images'),path('migrate/', views.migrate_images, name='migrate_images'),
]
