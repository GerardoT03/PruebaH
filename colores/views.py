from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import requests 
# Create your views here.


#-----"VISTA CONSUMO DE API"------#
def getAPI (request):
    URL_API = "https://django-etl-challenge.vercel.app/api/generate"
    response = requests.get(URL_API)

    if response.status_code == 200:
        programadores = response.json()
        agrupados_por_color={}

        for programador in programadores:
            color = programador.get( "color", "Desconocido")
            if color not in agrupados_por_color:
                agrupados_por_color[color]=[]
            agrupados_por_color[color].append(programador)

        return JsonResponse(agrupados_por_color, json_dumps_params={'indent': 4}, safe=False)
    return JsonResponse({"error":"No se pudo obtener la API"}, status=500)
    


#--------VISTA EN CASO DE IMPLEMENTAR UN ARCHIVO INDEX---------#
def obtener_programadores(request):
    URL_API = "https://django-etl-challenge.vercel.app/api/generate"
    try:
        response = requests.get(URL_API)
        if response.status_code==200:
            programadores = response.json()
        else:
            print(f'Error en la solicitud: {response.status_code}')
            programadores = []
    except request.RequestException as e:
        print(f"Error en la solicitud:{e}")
        productos =[] 

    return render(request,'index.html',{'programadores':programadores})
       

