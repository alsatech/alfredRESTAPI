from django.contrib import admin

# Register your models here.
from perfiles_api import models

admin.site.register(models.UserProfile)  #con esto le hemos dado acceso al administrador 
#para que pueda modificar modelos de UserProfile

