from rest_framework import serializers
from models import Buser

class BuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buser
        fields = '__all__'
