from django.contrib import admin

from . import models

admin.site.register(models.users)
admin.site.register(models.books)
admin.site.register(models.chapters)
admin.site.register(models.following)
admin.site.register(models.read)