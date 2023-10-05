from django.contrib import admin

from pages.models import Page, ContentType, Content

# Register your models here.
admin.site.register(Page)
admin.site.register(ContentType)
admin.site.register(Content)
