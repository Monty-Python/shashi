from django.contrib.auth.hashers import make_password, check_password
from django.forms.models import model_to_dict
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.settings import api_settings


from . import models

error_codes = {
    1: 'user exists',
}

actions = {
    1: 'new user created',
}


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class register(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        data = request.data

        user, created = models.users.objects.get_or_create(
            username = data['username'],
            email = data['email'],
            is_reader = data['reader'],
            is_author = data['author'],
            is_paid = data['paid']
        )

        if created:
            user.password = make_password(data['password'])
            user.save()
            msg = actions[1]
        else:
            msg = error_codes[1]
        
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({'msg':msg, 'token': token})