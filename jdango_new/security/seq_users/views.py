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
def suser_views(request):

    #print(f"######## GET id is {request.GET['id']} ########")
    #index = int(request.GET['id']) -1
    # = UserService().df_to_sql()
    #dic = [{'email':'p','nickname':'q','password':'1'},{'email':'2','nickname':'4','password':'5'}]
    #print(f'GET 리턴 결과 : {a}')
    data= SUserService().dataframe_create()
    ##[{'maximum_frequency_word': key}, {'maximum_frequency_count': value}]
    #ls = [{'maximum_frequency_word':key ,'maximum_frequency_count':value}]
    return JsonResponse({'result': data})