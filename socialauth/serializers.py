from . import googleauth
from rest_framework import serializers
from .register import register_social_user

import os
from rest_framework.exceptions import AuthenticationFailed




class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token= serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = googleauth.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise  serializers.ValidationError(
                'El token es invalido o expirado. Por favor ingresa de nuevo.'
            )
        if user_data['aud'] != os.environ.get('331660136567-cbervq49p9p57tr1blsg70oc7877rlt9.apps.googleusercontent.com'):

            raise  AuthenticationFailed(' Uy uy¿Quién es usted?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name)

