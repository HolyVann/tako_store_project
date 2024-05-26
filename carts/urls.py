from django.urls import path
from carts import views


app_name = 'carts'


urlpatterns = [
    path('cart-add-modal/', views.cart_add_modal, name='cart_add_modal'),
    path('cart-change-modal/', views.cart_change_modal, name='cart_change_modal'),
    path('cart-remove-modal/', views.cart_remove_modal, name='cart_remove_modal'),
    path('cart-change/', views.cart_change, name='cart_change'),
    path('cart-remove/', views.cart_remove, name='cart_remove'),
]
