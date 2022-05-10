from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .permissions import UpdateOwnProfile
from .models import UserProfile, ProfileFeedItem
from .serializers import UserProfileSerializer, ProfileFeedItemSerializer


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserProfileFeedViewSet(ModelViewSet):
    serializer_class = ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
