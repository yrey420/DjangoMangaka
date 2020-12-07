from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import os
import random
from rest_framework.exceptions import AuthenticationFailed





def generate_username(name):


    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username=username+str(random.randint(0,1000))
        return generate_username(random_username)




def register_social_user(provider, user_id, email, name):


    filtered_user_byEmail= User.objects.filter(email=email)

    if filtered_user_byEmail.exists():

        if provider == filtered_user_byEmail[0].auth_provider:

            registered_user = authenticate(
                email=email, password= os.environ.get('3GCkS_17AfKd7N0PM6382YG_')
            )


            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens()
            }

        else:
            raise AuthenticationFailed(
                detail='Continua tu inicio de sesión usando:  ' + filtered_user_byEmail[0])


    else:
        user = {
            'username': generate_username(name), 'email': email,
            'password': os.environ.get('3GCkS_17AfKd7N0PM6382YG_')}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('3GCkS_17AfKd7N0PM6382YG_'))
        return {
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens()
        }
