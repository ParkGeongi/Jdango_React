from rest_framework import serializers
from models import Theater_ticket

class Theater_ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater_ticket
        fields = '__all__'
