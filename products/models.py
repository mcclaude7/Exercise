from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

class Brand(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock_quantity = models.IntegerField()
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.URLField()
    created_date = models.DateField(auto_now_add=True)

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_review')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='id_product')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

class CartItem(models.Model):
    cart_id =models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_item')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_payment')
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    payment_date = models.DateField(auto_now_add=True)