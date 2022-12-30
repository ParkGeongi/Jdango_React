from rest_framework import serializers
from models import Delivery

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        medel = Delivery
        fields = '__all__'

