
from django.contrib import admin
from django.urls import path, include  #hacemos la inclusion 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('perfiles_api.urls')) 
]

'''
'''
