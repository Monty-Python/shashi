from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _


from . import models



class book_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.books
        fields = '__all__'



class chapter_serializer(serializers.HyperlinkedModelSerializer):
    book = book_serializer()

    class Meta:
        model = models.chapters
        fields = '__all__'
