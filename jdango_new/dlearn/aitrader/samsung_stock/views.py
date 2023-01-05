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

    start_day = request.GET['date']
    stock, pred_day = Samsung_Stock_Service().DNN_predict(start_day)
    a = [{'future': stock,'start_day':start_day,'pred_day':pred_day}]

    return JsonResponse({'result': a})

