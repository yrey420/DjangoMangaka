from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.



# Todas las clases siempre deben heredar de la clase padre en este caso Model
class LocalUser(AbstractUser):
    pass


