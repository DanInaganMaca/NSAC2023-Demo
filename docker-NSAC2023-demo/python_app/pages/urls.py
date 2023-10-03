from django.urls import path, include
from rest_framework import routers
from pages import views

# api versioning
router = routers.DefaultRouter()
router.register(r"pages", views.PageView, "pages")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/pages/by_code/<str:code>/",
         views.PageView.as_view({'get': 'get_by_code'}),
         name='page-get-by-code'),
]
