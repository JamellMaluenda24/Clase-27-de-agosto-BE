from django.shortcuts import render

# Create your views here.
def retornar_obtener_nuevo(request):
    return render(request, 'new_app/nuevo.html')

def obtener_listado(request):
    contenido = {
        'lista': [1,2,3],
        'otro_valor': 'tangamandapio'
    }
    return render(request, 'new_app/listado.html',contenido)
