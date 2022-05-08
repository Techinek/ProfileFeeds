from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

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


class HiViewSet(ViewSet):
    serializer_class = HiSeri

    def list(self, request):
        viewset_features = [
            'HTTP represented as functions: list, create, retrieve',
            'More functionality with less code',
            'Mapped to URLS'
        ]
        return Response({'message': 'Hi Viewset',
                         'features': viewset_features})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': name})
        else:
            return Response(serializer.errors,
                             status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'method': 'Retrieved GET'})

    def update(self, request, pk=None):
        return Response({'method': 'Updated PUT'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'Partial PATCH'})

    def destroy(self, request, pk=None):
        return Response({'method': 'Destroyed DELETE'})


