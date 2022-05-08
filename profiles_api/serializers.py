from rest_framework.serializers import ModelSerializer

from .models import UserProfile


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