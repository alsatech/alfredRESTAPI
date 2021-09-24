from django.db import models
# django trae sus modelos de usurarios , en django tienes que hacer login con usuario y nosotros lo haremos con email

from django.contrib.auth.models import AbstractBaseUser #clase basico de usuario de django
from django.contrib.auth.models import PermissionsMixin 
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    ''' Manager para perfiles de usuarios'''

    def create_user(self, email, name , password =None):
        ''' Crear nuevo User profile'''
        if not email:
            raise ValueError('Usuario debe tener un Email')

        email = self.normalize_email(email) 
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user 

    def create_superuser(self, email, name, password):  # ESTE ES UN ADMINISTRADOR 
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):   #hacemos herencia de abstract & permissions
    """ Modelo base de datos para usuarios en el sistema"""
    email = models.EmailField(max_length=225, unique= True) #campo unico no se puede repetir 
    name = models.CharField(max_length=225) #characterfield
    is_active = models.BooleanField(default=True)  # el usuario esta activo puede trabajar en la BD o p. web
    is_staff = models.BooleanField(default= False) #si son miembros del equipo 

    objects= UserProfileManager() 

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Obtener Nombre Completo del usuario'''
        return self.name

    def get_short_name(self):
        ''' Obtener nombre corto del usurario'''
        return self.name 

    def __str__(self) -> str:
        return self.email

    

    





