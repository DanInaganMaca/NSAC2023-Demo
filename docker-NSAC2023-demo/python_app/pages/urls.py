from django.urls import path, include
from rest_framework import routers
from pages import views

# api versioning
router = routers.DefaultRouter()
router.register(r"pages", views.PageView, "pages")

urlpatterns = [
    path("api/v1/", include(router.urls))
]
