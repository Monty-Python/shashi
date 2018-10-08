from django.contrib import admin

from . import models


class inlineFollowing(admin.TabularInline):
    model = models.following
    extra = 1


class inlineRead(admin.TabularInline):
    model = models.read
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = [inlineFollowing, inlineRead]

admin.site.register(models.users, UserAdmin)
admin.site.register(models.following)
admin.site.register(models.read)