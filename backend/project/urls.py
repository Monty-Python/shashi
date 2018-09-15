"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken import views as auth_view

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token




urlpatterns = [
    path('admin/', admin.site.urls),

    # url('get-auth-jwt', obtain_jwt_token),
    # url('refresh-auth-jwt', refresh_jwt_token),
    # url('verify-auth-jwt', verify_jwt_token),

    path('', include('users.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
