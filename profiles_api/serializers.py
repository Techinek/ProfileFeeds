from rest_framework import serializers


class HiSeri(serializers.Serializer):
    name = serializers.CharField(max_length=10)

