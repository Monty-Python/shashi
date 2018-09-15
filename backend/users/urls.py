from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views


urlpatterns = [
    url('register/', views.register.as_view()),
]