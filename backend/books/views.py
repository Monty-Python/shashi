from django.contrib.auth.hashers import make_password, check_password
from django.forms.models import model_to_dict
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models,serializers


class book(viewsets.ModelViewSet):
    queryset = models.books.objects.all()
    serializer_class = serializers.book_serializer
    # TODO add permissions
    permission_classes = ()



class chapter(viewsets.ModelViewSet):
    queryset = models.chapters.objects.all()
    serializer_class = serializers.chapter_serializer
    # TODO add permissions
    permission_classes = ()

    def create(self, request):
        book = models.books.objects.get(slug=request.data['book']['slug'])
        chapter, created = models.chapters.objects.get_or_create(book=book, chapter=request.data['chapter'])
        return Response(serializers.chapter_serializer(chapter, context={'request':request}).data)


