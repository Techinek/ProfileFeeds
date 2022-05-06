from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HiSeri


class HiApiView(APIView):
    serializer_class = HiSeri

    def get(self, request, format=None):
        django_api_features = [
            'HTTP represented as functions: get, post, patch, put, delete',
            'Similar to django view',
            'But for API',
            'Mapped to URLS'
        ]
        return Response({'greetings': 'Hello World',
                         'features': django_api_features})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})




