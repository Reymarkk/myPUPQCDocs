from rest_framework import serializers #importing rest framework into serializer.py
from .models import Orders #models from models.py


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'customer', 'product', 'email', 'address', 'mobile', 'order_date', 'status']