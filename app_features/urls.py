from django.urls import path
from app_features import views

urlpatterns = [
    path('', views.feature, name='feature'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),

    path('qr_mobile/<mobile>/<amount>/qr.png', views.get_qr, name='qr'),
    path('qr_nid/<nid>/<amount>/', views.get_qr, name='qr'),
    path('checkout/',views.checkout, name='checkout'),
    path('checkout/thankyou',views.checkout_thankyou, name='checkout_thankyou'),
]