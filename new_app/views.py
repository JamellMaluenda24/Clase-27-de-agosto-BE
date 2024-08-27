from django.shortcuts import render

# Create your views here.
def retornar_obtener_nuevo(request):
    return render(request, 'new_app/nuevo.html')