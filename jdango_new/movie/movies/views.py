from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from movie.movies.services import DcGan
# Create your views here.
@api_view(['GET'])
@parser_classes([JSONParser])
def fake_images(request):
    DcGan().fake_faces()
    print(f'Enter Show Faces with {request}')
    return JsonResponse({'Response Test' : 'SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def faces_blow_up(request):
    DcGan.faces_blow_up()
    print(f'Enter Show Faces with {request}')
    return JsonResponse({'Response Test' : 'SUCCESS'})