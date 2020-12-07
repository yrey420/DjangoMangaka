from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.validators import UniqueTogetherValidator


from mangas.models import Manga
from personas.models import LocalUser
from personas.views import login


class PersonaSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        localUser= LocalUser.objects.create_user(**validated_data)
        return localUser


    class Meta:
        model= LocalUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=LocalUser.objects.all(),
                fields=['username', 'email']
            )
        ]
class MangaSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        manga= Manga.objects.create_user(**validated_data)
        return manga

    class Meta:
        model=Manga
        fields=('id','nombreM', 'autorM', 'manga_sta')






