from rest_framework import serializers
from models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        medel = Order
        fields = '__all__'