from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ['name', 'description', 'address', 'email']


class ToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toys
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'telephone', 'address', 'is_exists']


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'


class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosOrder
        fields = '__all__'


class PosSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PosSupply
        fields = '__all__'