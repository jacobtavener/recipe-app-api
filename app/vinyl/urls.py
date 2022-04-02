from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vinyl import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'vinyl'

urlpatterns = [
    path('', include(router.urls)),
]
