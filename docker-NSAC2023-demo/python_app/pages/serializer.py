from rest_framework import serializers
from .models import Page, Content


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        # fields = ("id", "title", "description", "done")
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        # fields = ("id", "title", "description", "done")
        fields = "__all__"
