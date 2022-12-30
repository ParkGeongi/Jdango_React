from rest_framework import serializers
from models import Suser

class SuserSerializer(serializers.ModelSerializer):
    class Meta:
        medel = Suser
        fields = '__all__'
