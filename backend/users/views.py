from django.contrib.auth.hashers import make_password, check_password
from django.forms.models import model_to_dict
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models,serializers
from books import models as book_models
from books import serializers as book_serializers


class register(viewsets.ModelViewSet):
    queryset = models.users.objects.all()
    serializer_class = serializers.client_serializer
    permission_classes = ()



class follow(viewsets.ModelViewSet):
    queryset = models.following.objects.all()
    serializer_class = serializers.follow_serializer
    # TODO add permissions
    permission_classes = ()

    def create(self, request):
        user = models.users.objects.get(user=User.objects.get(username=request.user))
        book = book_models.books.objects.get(slug=request.data['book'])
        follow, created = models.following.objects.get_or_create(user=user)
        follow.books.add(book)
        return Response([item.slug for item in model_to_dict(follow)['books']])

    
    def delete(self, request):
        user = models.users.objects.get(user=User.objects.get(username=request.user))
        book = book_models.books.objects.get(slug=request.data['book'])
        follow, created = models.following.objects.get_or_create(user=user)
        follow.books.remove(book)
        return Response([item.slug for item in model_to_dict(follow)['books']])




class read(viewsets.ModelViewSet):
    http_method_names = ['get','post']
    queryset = models.read.objects.all()
    serializer_class = serializers.read_serializer
    # TODO add permissions
    permission_classes = ()

    def create(self, request):
        user = models.users.objects.get(user=User.objects.get(username=request.user))
        book = book_models.books.objects.get(slug=request.data['book'])
        chapter = book_models.chapters.objects.get(book=book, chapter=request.data['chapter'])
        user_read, created = models.read.objects.get_or_create(user=user, book=book)
        user_read.chapter.add(chapter)
        data = {}
        data['book'] = book_serializers.book_serializer(book, context={'request':request}).data
        data['chapters'] = [item.chapter for item in model_to_dict(user_read)['chapter']]
        return Response(data)