from rest_framework import serializers
from .models import Category, Product, Brand, Review, Order, OrderItem, Cart, CartItem, Payment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only = True)
    category = CategorySerializer(read_only = True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'stock_quantity', 'brand', 'category','image', 'created_date']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    product = ProductSerializer(read_only = True)

    class Meta:
        model = Review
        fields = ['rating', 'comment', 'user', 'product']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = Order
        fields = ['user', 'order_date','status']

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['order','product','quantity','price']

class CartSerializer(serializers.ModelSerializer):
    ...

class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['cart','product','quantity', 'price']

class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only = True)

    class Meta:
        model = Payment
        fields = ['order','amount','payment_method','payment_date']