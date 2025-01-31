from django.urls import path
from .views import getAPI, obtener_programadores

urlpatterns = [
    #path('',obtener_programadores,name='obtener_programadores'), #---"FALTA EL CODIGO EN EL HTML"---#
    path('api/',getAPI,name='get_api')
]
