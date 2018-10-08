from django.contrib import admin

from . import models


class inlineChapter(admin.TabularInline):
    model = models.chapters
    extra = 1



class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [inlineChapter]

admin.site.register(models.books, BookAdmin)
