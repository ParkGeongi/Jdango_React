from rest_framework import serializers
from models import MUser

class MUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MUser
        fields = '__all__'