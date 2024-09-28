from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def crear_curso(req, nombre, camada):
    
    nuevo_curso = Curso(nombre=nombre, camada=camada)
    nuevo_curso.save()
    
    return HttpResponse(f"""
                        <p>Curso: {nuevo_curso.nombre} - Camada: {nuevo_curso.camada} creado con éxito</p>
                        """)
    
def lista_cursos(req):
    
    lista = Curso.objects.all()
    
    return render(req, "lista_cursos.html", {"lista_cursos" : lista})