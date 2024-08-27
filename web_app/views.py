from django.shortcuts import render

# Create your views here.
def retornar_vista_ejemplo(request):
    return render(request, 'web_app/vista_ejemplo.html')