import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from security.seq_users.repositories import SeqUserRepository
from security.seq_users.serializers import SeqUserSerializer
from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def sequser(request):
    if request.method == 'POST':
        new_user = request.data
        print(f"리액트에서 들옥한 신규 사용자 {new_user}")
        serializer = SeqUserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result' : 'SUCCESS'})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'PUT':
        repo = SeqUserRepository()
        modify_user = repo.find_user_by_email(request.data["user_email"]) # 리액트
        db_user = repo.find_by_id(modify_user.id)
        serializer = SeqUserSerializer(data=db_user)
        if serializer.is_valid():
            serializer.update(modify_user,db_user)
            return JsonResponse({'result' : 'SUCCESS'})

    elif request.method == 'DELETE':
        repo = SeqUserRepository()
        delete_user = repo.find_user_by_email(request.data["user_email"])  # 리액트
        db_user = repo.find_by_id(delete_user.id)
        db_user.delete()
        return JsonResponse({'result': 'SUCCESS'})
    elif request.method == 'GET':
        return Response(SeqUserRepository().find_user_by_email(request.data['user_email']))

@api_view(["GET"])
@parser_classes([JSONParser])
def sequser_list(request):
    return SeqUserRepository().get_all()



@api_view(["POST"])
@parser_classes([JSONParser])
def login_seq(request):
    return SeqUserRepository().login(user_email = request.data['user_email'],password = request.data['password'])


@api_view(["GET"])
@parser_classes([JSONParser])
def list_by_name(request):
    return  Response(SeqUserRepository().find_user_by_name(request.data["user_name"]))

@api_view(["GET"])
@parser_classes([JSONParser])
def list_by_name(request):
    return  Response(SeqUserRepository().find_user_by_name(request.data["job"]))