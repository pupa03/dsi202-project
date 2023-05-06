from django.db import models
from django.contrib.auth.models import User

import uuid
from app_users.models import CustomUser
# Create your models here.


class Feature(models.Model):
    Feature_Category = (
        ("MUSIC","MUSIC"),
        ("MOVIE","MOVIE")
    )

    name = models.CharField(max_length=60)
    category = models.CharField(max_length=5, choices=Feature_Category, default="MOVIE")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="")
    image = models.ImageField(upload_to="images/features", default="")

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user: CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='carts')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
    
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
    

class CartItem(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name="items")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.feature.name
    
    @property
    def price(self):
        new_price = self.feature.price * self.quantity
        return new_price
    


class ImageModel(models.Model):
    image = models.ImageField(upload_to="images/slip")

    def __str__(self):
        return self.image





