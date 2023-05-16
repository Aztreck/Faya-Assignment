from rest_framework import serializers
from .models import Customer, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'is_active', 'registered_at')

class CustomerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'created_at', 'updated_at', 'products')
