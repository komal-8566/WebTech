from django.contrib import admin
from .models import Category,Products,Toppings,CartItem,Placed_Order,Reviews
# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Toppings)
admin.site.register(CartItem)
admin.site.register(Placed_Order)
admin.site.register(Reviews)