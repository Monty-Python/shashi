from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken import views as auth_view

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from users import views as user_views
from books import views as book_views

router = routers.DefaultRouter()

# create,edit,view,delete user
router.register('register', user_views.register)

# create,edit,view,delete book
router.register('book', book_views.book)

# create,edit,view,delete chapter of book
router.register('chapter', book_views.chapter)

# create,edit,view,delete followers of book
router.register('follow', user_views.follow)

# create,edit,view,delete readers of book
router.register('read', user_views.read)


urlpatterns = [
    path('admin/', admin.site.urls),

    url('get-auth-jwt', obtain_jwt_token),
    url('refresh-auth-jwt', refresh_jwt_token),
    url('verify-auth-jwt', verify_jwt_token),

    url('',include(router.urls)),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

