from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status

from perfiles_api import serializers


class HelloApiView(APIView):
    ''' API View de prueba'''
    serializer_class = serializers.HelloSerializer

    def get (self, request, format=None):     
        '''Retornar lista de caractericsticas del APIView'''

        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put , delete )',
            'Es similar a una vista tradicional  de Django',
            'Nos da el mayor control sobre la logica sobre de nuestra aplicacion ',
            'Esta mapeado manualmente a los URLs',

        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
        #esta informacion de respuesta la va convertir en un formato json, debe ser una lista o diccionario

    def post(self, request):
        '''Crear un mensaje con nuestro nombre'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer._validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST 

            )
    def put ( self, request, pk=None):
        ''' Maneja actualizar un objeto'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''Maneja actualizacion parcial de un objeto '''
        return Response ({'method': 'PATCH'})

    def delete(self, request, pk=None):
         '''Borrar un Objeto'''
         return Response({'method': 'DELETE'})
         

         
    
       


    
    



            



