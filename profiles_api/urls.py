from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserLoginApiView, UserProfileFeedViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
router.register('feed', UserProfileFeedViewSet)

urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
]
