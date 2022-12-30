import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from security.seq_users.models import SeqUser
from security.seq_users.serializers import SeqUserSerializer
from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token



class SeqUserRepository(object):
    def __init__(self):
        pass

    def select_all(self):
        serializer = SeqUserSerializer(SeqUser.objects.all(), many=True)
        return Response(serializer.data)

    def login(self, **keyargs):
        loginUser = SeqUser.objects.get(user_email=keyargs['user_email'])
        print(f"해당 email 을 가진  User: {loginUser}")

        if loginUser.password == keyargs["password"]:
            dbUser = SeqUser.objects.all().filter(susers_id=loginUser.susers_id).values()[0]
            print(f'DBUser is {dbUser}')
            serializer = SeqUserSerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        else:
            return JsonResponse({'data': 'PASSWORD WRONG'})



