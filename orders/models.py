from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  name= models.CharField(max_length=64)
  def __str__(self):
    return f'{self.name}'

class Products(models.Model):
  product_type=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='type')
  name=models.CharField(max_length=64)
  small_price = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
  large_price = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True) 
  max_toppings = models.IntegerField(default=0,null=True)
  def __str__(self):
    res={'product_type':self.product_type,'name':self.name,'small':self.small_price,'large':self.large_price,'max_toppings':self.max_toppings}
    return f'"product_type":{self.product_type}, "name":{self.name}, "small":{self.small_price}, "large":{self.large_price}, "max_toppings":{self.max_toppings}'

  def is_pizza(self):
    if str(self.product_type)=='Regular Pizza' or str(self.product_type)=='Sicilian Pizza':
      return True
    return False

class Toppings(models.Model):
  name=models.CharField(max_length=64)
  def __str__(self):
    return f'{self.name}'

class CartItem(models.Model):
  user_id=models.IntegerField()
  order_no=models.IntegerField(null=True,blank=True)
  category = models.CharField(max_length=64)
  subcategory=models.CharField(max_length=64)
  price=models.DecimalField(max_digits=5,decimal_places=2)
  size=models.CharField(max_length=10,default='N/A')
  topping1=models.CharField(max_length=64,null=True,blank=True)
  topping2=models.CharField(max_length=64,null=True,blank=True)
  topping3=models.CharField(max_length=64,null=True,blank=True)
  topping4=models.CharField(max_length=64,null=True,blank=True)
  topping5=models.CharField(max_length=64,null=True,blank=True)

  def __str__(self):
    return f'"order_no":{self.order_no} "user_id":{self.user_id}, "category":{self.category}, "subcategory":{self.subcategory}, "price":{self.price},"toppings":{self.topping1},{self.topping2},{self.topping3},{self.topping4},{self.topping5} '

class Placed_Order(models.Model):
  STATUS=(('Pending','Pending'),('Delivered','Delivered'))
  order_no=models.IntegerField()
  user_id=models.IntegerField()
  status=models.CharField(max_length=10,choices=STATUS,default='Pending')
  date_time=models.DateTimeField(auto_now=True)
  def __str__(self):
    return f'Order number {self.order_no} for user id {self.user_id} placed at {self.date_time} is {self.status}'
  def is_pending(self):
    if str(self.status) == 'Pending':
      return True
    return False

class Reviews(models.Model):
  user_id=models.IntegerField()
  name = models.CharField(max_length=20, null= True)
  description=models.CharField(max_length=300)
  star = models.IntegerField(null=True)

  def __str__(self):
    return f'"user_id":{self.user_id} "name":{self.name} "description":{self.description}'