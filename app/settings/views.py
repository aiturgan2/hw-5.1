from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.settings.models import Settings
from app.settings.serializers import SettingsSerializer

class SettingsListAPIView(APIView):

    def get(self, request, key=None):
        if key:
            try:
                instance = Settings.objects.get(key=key)
            except Settings.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = SettingsSerializer(instance)
            return Response(serializer.data)

        queryset = Settings.objects.all().order_by("key")
        serializer = SettingsSerializer(queryset, many=True)
        return Response(serializer.data)

class SettingsCreateAPIView(APIView):
    def post(self, request):
        serializer = SettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicSettingsAPIView(APIView):
    def get(self, request, key=None):
        if key:
            try:
                instance = Settings.objects.get(key=key, is_public=True)
            except Settings.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = SettingsSerializer(instance)
            return Response(serializer.data)

        queryset = Settings.objects.filter(is_public=True).order_by("key")
        serializer = SettingsSerializer(queryset, many=True)
        return Response(serializer.data)