from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from dlearn.aitrader.samsung_stock.services import Samsung_Stock_Service


# Create your views here.
@api_view(["GET"])
@parser_classes([JSONParser])
def Samsung_stock(request):

    da = request.GET['date']
    print(da)

    s = Samsung_Stock_Service().hook()
    return JsonResponse({'data': s})


