
from django.conf.urls import include
from django.urls import path
from . import views


app_name = "JAGUARETE"
urlpatterns = [
    # path('', views.Home,name="Home"),
    path('Home', views.Home, name="Home"),
    path('Registro', views.Registro, name="Registro"),
    path('Acercade', views.Acercade, name="Acercade"),

    path('Login', views.Login, name="Login"),
    path('Buscador', views.Buscador, name="Buscador"),
    path('Carrito', views.Carrito, name="Carrito"),
    path('Producto', views.Producto, name="Producto"),
    path('AgreProd', views.AgreProd, name="AgreProd"),
    path('Contacto', views.Contacto, name="Contacto")
]
