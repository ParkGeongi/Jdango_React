from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from blog.posts.models import Post
from blog.posts.serializers import PostSerializer
from blog.tags.models import Tag
from blog.tags.serializers import TagSerializer


class TagRepository(object):

    def __init__(self):
        print(" CommentsRepository 객체 생성 ")

    def get_all(self):
        return Response(TagSerializer(Tag.objects.all(), many=True).data)

    def find_by_id(self, id):
        return Response(TagSerializer(Tag.objects.all(), many=True).data)