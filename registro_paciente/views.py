from django.contrib.postgres.search import SearchQuery , SearchVector , SearchRank
from django.forms import formset_factory
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect,FileResponse
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from django.shortcuts import render , redirect , get_object_or_404
from .forms import RegistroDosForm,LoginForm,ResultadosForm,PruebasForm,PruebasFormSet,BusquedaForm
from django.forms import modelformset_factory
from .models import Registro,Pruebas,PersonalModel
from django.db.models import Q
import io
from xhtml2pdf import pisa
from io import BytesIO

# Create your views here.

def home(request):

    return render(request,"sistema/home.html")

def login(request):
    if request.method == 'POST':
       form = LoginForm(request, data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('registro_de_citas')
    else:
       form = LoginForm()
    return render(request,"sistema/loggin.html")

def registro_de_citas(request):
    context = {}

    if request.method == 'POST':
        formRegistro = RegistroDosForm(request.POST, request.FILES)
        if formRegistro.is_valid():
            registro = formRegistro.save(commit=False)
            
            # Obtener pruebas adicionales
            pruebas_adicionales = request.POST.getlist('prueba_adicional')
            
            # Calcular el costo total incluyendo pruebas adicionales
            costo_total = calcular_costo_total(registro.prueba, registro.necesita_factura)
            for prueba_adicional in pruebas_adicionales:
                costo_total += calcular_costo_total(prueba_adicional, registro.necesita_factura)
            
            registro.costo_total = costo_total
            registro.save()

            # Generar PDF con el costo total
            buffer = generar_pdf_archivo(registro, costo_total)
            return FileResponse(buffer, as_attachment=True, filename="nombre.pdf")
    else:
        formRegistro = RegistroDosForm()

    context['formRegistro'] = formRegistro
    return render(request, "sistema/registro_de_citas.html", context)


def calcular_costo_total(prueba, necesita_factura):
    costo = Pruebas.objects.filter(Q(nombre__icontains=prueba)).first().costo
    
    if necesita_factura:
        costo *= 1.16
    
    return costo


def generar_pdf_archivo(registro,costos):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    elements = []
    styles = getSampleStyleSheet()

    # Estilo para los títulos
    title_style = styles['Title']
    title_style.textColor = colors.darkblue
    title_style.fontSize = 18
    elements.append(Paragraph("<b>CITA AGENDADA</b>", title_style))

    elements.append(Spacer(1, 20))
    # Estilo para el contenido
    content_style = styles['BodyText']
    content_style.spaceBefore = 10
    elements.append(Image('registro_paciente/static/sistema/logo_vive_login.png', width=200, height=100))
    elements.append(Spacer(1, 20))
    field_title_style = ParagraphStyle('field_title', parent=content_style, textColor=colors.darkblue, fontSize=12, spaceBefore=6)
    elements.append(Paragraph("<b>Información del paciente:</b>", field_title_style))
    elements.append(Paragraph(f"<b>Nombre:</b> {registro.nombre}", content_style))
    elements.append(Paragraph(f"<b>Apellido Paterno:</b> {registro.apellido_paterno}", content_style))
    elements.append(Paragraph(f"<b>Apellido Materno:</b> {registro.apellido_materno}", content_style))
    elements.append(Paragraph(f"<b>Género:</b> {registro.genero}", content_style))
    elements.append(Paragraph(f"<b>Teléfono:</b> {registro.telefono}", content_style))
    elements.append(Paragraph(f"<b>Edad:</b> {registro.edad}", content_style))

    elements.append(Spacer(1, 20))

    elements.append(Paragraph("<b>Información de la cita:</b>", field_title_style))
    elements.append(Paragraph(f"<b>Prueba:</b> {registro.prueba}", content_style))
    elements.append(Paragraph(f"<b>Diagnóstico:</b> {registro.diagnostico}", content_style))
    elements.append(Paragraph(f"<b>Doctor:</b> {registro.doctor}", content_style))
    elements.append(Paragraph(f"<b>Fecha:</b> {registro.fecha}", content_style))

    elements.append(Spacer(1, 20))

    # Mostrar el costo de la prueba original
    elements.append(Paragraph(f"<b>Costo Original:</b> ${costos[0]:.2f}", content_style))

    # Mostrar el costo de las pruebas adicionales
    for i, costo_adicional in enumerate(costos[1:], start=1):
        elements.append(Paragraph(f"<b>Costo Adicional {i}:</b> ${costo_adicional:.2f}", content_style))

    # Calcular y mostrar el costo total
    costo_total = sum(costos)
    elements.append(Paragraph(f"<b>Costo Total:</b> ${costo_total:.2f}", content_style))

    doc.build(elements)
    buffer.seek(0)

    return buffer




def resultados(request):
   form = ResultadosForm()
   if request.method == 'POST':  # Verifica si el formulario ha sido enviado
        form = ResultadosForm(request.POST)  # Crea un formulario con los datos ingresados por el usuario
        if form.is_valid():  # Verifica si el formulario es válido
            nombre = form.cleaned_data['busqueda']  # Obtiene el nombre ingresado por el usuario desde el formulario
            resultados = Registro.objects.filter(nombre__icontains=nombre)  # Filtra los registros basados en el nombre
            
            # Aquí puedes hacer algo con los resultados, como enviarlos al formulario
            # Pero primero, asegurémonos de entender qué está sucediendo aquí

            # Retornamos los resultados al template para que se muestren
            return render(request, "sistema/resultados.html", {'form': form, 'resultados': resultados, 'busqueda': nombre})

        else:  # Si no se ha enviado el formulario, simplemente renderizamos el formulario en blanco
         form = ResultadosForm()

   return render(request, "sistema/resultados.html", {'form': ResultadosForm()})

def buscador(request):
    context = {}
    resultados = []
    query = None

    if request.method == 'POST':
        PruebasFormSet = formset_factory(PruebasForm, extra=1)
        formset = PruebasFormSet(request.POST)
        
        if formset.is_valid():
            # Recorrer el formset para obtener los datos
            for form in formset:
                query = form.cleaned_data.get('search_query')
                if query:
                    busqueda = SearchQuery(query)
                    resultados.extend(Pruebas.objects.filter(nombre__search=busqueda))

        context['formset'] = formset

    context['resultados'] = resultados
    context['query'] = query
    return render(request, "sistema/buscador.html", context)


def resultadoReferenciados(request):
    resultados = []
    query = request.GET.get('q')
    iva = 0.16
    seleccion_iva = request.GET.get('incrementar_iva')

    if query:
           busqueda = SearchQuery(query)
           resultados = Pruebas.objects.filter(nombre__search=busqueda)
    for prueba in resultados:
        if seleccion_iva == 'si':
            prueba.costo+=prueba.costo*iva       
    return render(request, 'sistema/resultadosReferenciados.html', {'resultados': resultados, 'query': query})

def crear_registro(request):
    if request.method == 'POST':
        registro_form = RegistroDosForm(request.POST, prefix='registro')
        pruebas_formset = PruebasFormSet(request.POST, prefix='pruebas')
        if registro_form.is_valid() and pruebas_formset.is_valid():
            registro = registro_form.save()
            pruebas = pruebas_formset.save(commit=False)
            for prueba in pruebas:
                prueba.registro_asociado = registro  # Asignamos el registro a cada prueba
                prueba.save()
            # Realizar acciones adicionales después de guardar los registros
    else:
        registro_form = RegistroDosForm(prefix='registro')
        pruebas_formset = PruebasFormSet(queryset=Pruebas.objects.none(), prefix='pruebas')

    # Aquí es donde podrías implementar la lógica de búsqueda
    search_query = request.GET.get('search_query')  # Obtener el parámetro de búsqueda del request

    if search_query:
        # Realizar la búsqueda utilizando el nombre y el costo
        pruebas = Pruebas.objects.filter(nombre__icontains=search_query)  # Filtrar por nombre
        pruebas = pruebas.filter(costo__icontains=search_query)  # Filtrar por costo
        # Puedes pasar los resultados de la búsqueda al contexto
        return render(request, 'sistema/crear_registro.html', {'registro_form': registro_form, 'pruebas_formset': pruebas_formset, 'pruebas': pruebas, 'search_query': search_query})
    else:
        return render(request, 'sistema/crear_registro.html', {'registro_form': registro_form, 'pruebas_formset': pruebas_formset})