from django.contrib import admin

# Register your models here.
from  personas.models import LocalUser


admin.site.register(LocalUser)