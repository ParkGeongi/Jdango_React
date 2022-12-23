from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from blog.busers.services import UserService


# Create your views here.

@api_view(["GET"])
@parser_classes([JSONParser])
def blog_login(request):

    #print(f"######## GET id is {request.GET['id']} ########")
    #index = int(request.GET['id']) -1
    # = UserService().df_to_sql()
    #dic = [{'email':'p','nickname':'q','password':'1'},{'email':'2','nickname':'4','password':'5'}]
    #print(f'GET 리턴 결과 : {a}')
    data = UserService().Dataframe_create()
    return JsonResponse({'result': data})
