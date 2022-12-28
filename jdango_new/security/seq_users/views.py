from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from blog.busers.services import UserService
from nlp.samsung_report.services import Controller
from security.seq_users.services import SUserService


# Create your views here.
@api_view(["GET"])
@parser_classes([JSONParser])
def list(request):
    data= SUserService().to_react()
    return JsonResponse({'result': data})


@api_view(["GET"])
@parser_classes([JSONParser])
def suser_views(request):
    SUserService().get_users()
    return JsonResponse({'result': 'Success'})

def login(request):
    pass