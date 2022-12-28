from rest_framework import serializers
from models import Cinemas


class CinemasSerializer(serializers.ModelSerializer):
    class Meta:
        medel = Cinemas
        fields = '__all__'
