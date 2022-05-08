from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import HiApiView, HiViewSet

router = DefaultRouter()
router.register('viewset', HiViewSet, basename='viewset')

urlpatterns = [
    path('apiview/', HiApiView.as_view(), name='api-view'),
    path('', include(router.urls))
]
