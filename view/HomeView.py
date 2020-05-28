from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():
    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())

    def pagina1(self):
        return HttpResponse('Hola desde una nueva ruta')

    def pagina2(self, parametro1):
        return HttpResponse('Hola de nuevo ' + str(parametro1))

    def pagina3(self, parametro1, parametro2):
        return HttpResponse('Hola de nuevo ahora con dos '+str(parametro1) + ' - ' + str(parametro2))

    def formulario(self):
        plantilla = get_template('formulario.html')
        return HttpResponse(plantilla.render())

    def formulario2(self):
        plantilla = get_template('formulario2.html')
        return HttpResponse(plantilla.render())

    def formulario3(self):
        plantilla = get_template('formulario3.html')
        return HttpResponse(plantilla.render())

    def formulario4(self):
        plantilla = get_template('formulario4.html')
        return HttpResponse(plantilla.render())

    def formulario5(self):
        plantilla = get_template('formulario5.html')
        return HttpResponse(plantilla.render())