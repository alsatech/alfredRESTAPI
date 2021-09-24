from django.urls import path
from django.urls import path

from perfiles_api import views

urlpatterns = [
    path ('hello-view/', views.HelloApiView.as_view()), 
    #cargamos la clase helloapiview como funcion por eso el as.view
]



