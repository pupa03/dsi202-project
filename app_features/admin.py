from django.contrib import admin
from app_features.models import Feature, Cart, CartItem, ImageModel

# Register your models here.

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc']
    search_fields = ['name']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['feature', 'cart']


admin.site.register(Feature, FeatureAdmin)
admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(ImageModel)