from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import make_password


from . import models
from books import serializers as book_serializers



class User_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']



class client_serializer(serializers.HyperlinkedModelSerializer):
    user = User_Serializer()

    class Meta:
        model = models.users
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = User.objects.create_user(**validated_data['user'])
        client = models.users.objects.create(**validated_data)
        return client


class follow_serializer(serializers.HyperlinkedModelSerializer):
    user = User_Serializer()
    following = book_serializers.book_serializer()

    class Meta:
        model = models.following
        fields = '__all__'


class read_serializer(serializers.HyperlinkedModelSerializer):
    user = User_Serializer()
    book = book_serializers.book_serializer()
    chapter = book_serializers.chapter_serializer()

    class Meta:
        model = models.read
        fields = '__all__'