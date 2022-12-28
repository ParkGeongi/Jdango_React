from rest_framework import serializers
from models import SeqUser

class SeqUserSerializer(serializers.ModelSerializer):
    class Meta:
        medel = SeqUser
        fields = '__all__'
        