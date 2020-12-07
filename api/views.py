from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from api.serializers import PersonaSerializer
from api.serializers import MangaSerializer
from personas.models import LocalUser
from mangas.models import Manga


class PersonasRecordView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        localUser = LocalUser.objects.all()
        serializer = PersonaSerializer(localUser, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )



class MangasTodo(generics.ListCreateAPIView):
    queryset= Manga.objects.all()
    serializer_class = MangaSerializer

class MangaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

