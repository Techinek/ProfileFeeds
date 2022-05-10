from rest_framework.serializers import ModelSerializer

from .models import UserProfile, ProfileFeedItem


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Triggers custom create_user function of UserProfileManager"""
        user = UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password'])

        return user


class ProfileFeedItemSerializer(ModelSerializer):

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }
