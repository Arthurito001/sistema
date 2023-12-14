from django.urls import path 

from . import views


urlpatterns = [
    #path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('registro_de_citas/', views.registro_de_citas, name = 'registro_de_citas'),
    path('resultados/', views.resultados, name = 'resultados'),
    path('login/', views.login, name = 'login'),
    path('resultadosReferenciados/', views.resultadoReferenciados, name = 'resultadosReferenciados'),
    path('buscador/', views.buscador, name= 'buscador'),
    path('crear_registro/', views.crear_registro, name='crear_registro'),
    #path('generar_pdfResultados/', views.generar_pdfResultados, name='generar_pdfResultados'),
    #path('', views.saludos)

]