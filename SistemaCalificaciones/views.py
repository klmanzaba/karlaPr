from django.shortcuts import render, HttpResponse

# Create your views here.
def bienvenido (resquest, plantilla= "bienvenido.html"):
    return render(resquest,plantilla)
def contactanos(resquest, plantilla= "contactanos.html"):
    return render(resquest, plantilla)
def acercade(resquest, plantilla= "acercade.html"):
    return render(resquest, plantilla)
#CREAMOS LA BASE HTML PARA MENUS EN HTML
#DE ESTA MANERA AGRAGAMOS MENU

html_base = """
    <h1>FUNDACION YOUNG LIVING SISTEMA WEB </h1>
    <ul>
        <li>   <a href="/">FUNDACION YOUNG LIVING</a>              </li>
        <li>   <a href="/contact/">CITAS</a>     </li>
        <li>   <a href="/contact/">HORARIOS</a>     </li>
        <li>   <a href="/contact/">Ubicanos</a>     </li>
        <li>   <a href="/about-me/">ACERCA DE NOSOTROS</a>   </li>
        <li>   <a href="/contact/">CONTACTANOS</a>     </li>
    </ul>
"""

#DEFINIMOS LAS HTML

def bienvenido(request):
    html_responsde = "<h1>FUNDACION YOUNG LIVING</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def contactanos(request):
    html_responsde = "<h1>CONTACTANOS 0968866760</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def acercade(request):
    html_responsde = "<h1> ACERCA DE NOSOTROS - EDUCACION - REGISTRO DE CALIFICACIONES , SERVICIO GARANTIZADO <br> - SE OFRECE SERVICIOS DE EDUCACION Y CAPACITACION <br> - EDUCACION A PERSONAS CON DISCAPACIDAD <br> - APRENDIZAJE Y PRACTICA <br> - CONSULTAS DE MATRICULAS <br> - CURSOS Y LABORATORIOS <br> - CONVENIOS</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);
