from django.urls import path, include
from rest_framework.routers import DefaultRouter

from album import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('artists', views.ArtistViewSet)

app_name = 'album'

urlpatterns = [
    path('', include(router.urls)),
]
