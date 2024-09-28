from django.http import HttpResponse
from django.template import loader

def bucles_condicionales(req):
    template = loader.get_template("template_condicionales.html")
    document = template.render({
        "notas" : [2, 5, 9, 10, 3, 11]
    })
    return HttpResponse(document)