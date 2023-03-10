from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from blog.posts.repositories import PostRepository
from blog.posts.serializers import PostSerializer

# Create your views here.
# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def post(request):
        if request.method == 'POST':
                return PostSerializer().create(request.data)
        elif request.method == 'PATCH':
                return None
        elif request.method == 'PUT':
                return PostSerializer().update(request.data)
        elif request.method == 'DELETE':
                return PostSerializer().delete(request.data)
        elif request.method == 'GET':
                return PostRepository().find_by_id(request.data)

@api_view(["GET"])
@parser_classes([JSONParser])
def post_list(request):
        return PostRepository().get_all()



