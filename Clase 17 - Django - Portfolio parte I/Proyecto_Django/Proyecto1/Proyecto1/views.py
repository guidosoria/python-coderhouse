from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def saludo(req):
    return HttpResponse("Bienvenido a mi primer proyecto!")

def proyecto_html(req):
    escuela = "Coderhouse"
    return HttpResponse(
    f"""
    <h1>Bienvenido a mi primer proyecto de Django</h1>
    <h3>Esto forma parte del cuso de Python de {escuela} </h3>
    """
    )
    
def dia_de_hoy(req):
    hoy = datetime.now()
    texto = f'Hoy es: {hoy}'
    return HttpResponse(texto)

def saluda_con_nombre(req, nombre):
    return HttpResponse(f'Hola {nombre}')

def probando_template(req, name):
    
    # html = open("/Users/gsoria/Documents/Learning/Python/Python - Coderhouse/Clase 17 - Django - Portfolio parte I/Proyecto_Django/Proyecto1/Proyecto1/templates/template1.html")
    # plantilla = Template(html.read())
    # html.close()
    # contexto = Context({
    #  "name" : "Guido",
    #  "curso" : "Python",   
    #  "escuela" : "Coderhouse",
    #  "notas" : [2, 4, 10, 12, 11, 9]
    # })
    # documento = plantilla.render(contexto)
    
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render({
     "name" : name,
     "curso" : "Python",   
     "escuela" : "Coderhouse",
     "notas" : [2, 4, 10, 12, 11, 9]
    })
    
    return HttpResponse(documento)
    
        
    