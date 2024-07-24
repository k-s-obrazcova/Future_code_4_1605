from rest_framework import serializers
from .models import *
from django import forms


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'buyer_lastname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish',
            'product'
        ]


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'create_date',
            'update_date',
            'photo',
            'is_exists',
            'warehouse',
            'parametr',
            'category',
            'tag',
        ]


class ProductSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = [
            'date_supply',
            'supplier',
            'product'
        ]


class ParametrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametr
        fields = [
            'name'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name',
            'description'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    single_position = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)

    class Meta:
        model = Inventory
        fields = [
            'product',
            'warehouse',
            'quantity',
            'single_position'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'product',
            'user_name',
            'rating',
            'comment',
            'photo'
        ]
