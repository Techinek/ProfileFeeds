from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from .permissions import UpdateOwnProfile
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
