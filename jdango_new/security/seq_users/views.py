import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from security.seq_users.models import SeqUser
from security.seq_users.repositories import SeqUserRepository
from security.seq_users.serializers import SeqUserSerializer
from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(["GET"])
@parser_classes([JSONParser])
def list(request):
    data= SeqUserService().to_react()
    return JsonResponse({'result': data})

@api_view(["GET"])
@parser_classes([JSONParser])
def SeqUser_views(request):
    if request.method == 'GET':
        return SeqUserRepository().select_all()

@api_view(["POST"])
@parser_classes([JSONParser])
def seqlogin(request):
        print(f'로그인 정보 : {request.data}')
        return SeqUserRepository().login(user_email = request.data['user_email'],password = request.data['password'])


# dictionary이외를 받을 경우, 두번째 argument를 safe=False로 설정해야한다.
