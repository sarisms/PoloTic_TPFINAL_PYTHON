from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django import forms
from django.urls import reverse


# Create your views here.
class FormAltaProd(forms.Form):
    product = forms.CharField(label="Agregar Producto")


def Producto(request):
    if "productos" not in request.session:
        request.session["productos"] = []
    return render(request, "JAGUARETE/Producto.html", {
        'productos': request.session["productos"]
    })


def Registro(request):

    return render(request, "JAGUARETE/Registro.html")


def Acercade(request):

    return render(request, "JAGUARETE/Acercade.html")


def Buscador(request):

    return render(request, "JAGUARETE/Buscador.html")


def Carrito(request):

    return render(request, "JAGUARETE/Carrito.html")


def Login(request):

    return render(request, "JAGUARETE/Login.html")


def AgreProd(request):
    if request.method == "POST":
        form = FormAltaProd(request.POST)
        if form.is_valid():
            product = form.cleaned_data["product"]
            request.session["productos"] += [product]
            return HttpResponseRedirect(reverse("JAGUARETE:Producto"))
        else:
            return render(request, "JAGUARETE/AgreProd.html")
    else:
        return render(request, "JAGUARETE/AgreProd.html")


def Home(request):

    return render(request, "JAGUARETE/Home.html")


def Contacto(request):

    return render(request, "JAGUARETE/Contacto.html")
