from django.shortcuts import render, redirect
from ventacarta.models import Usuario, Carta

# Create your views here.


def home(request):
    return render(request, 'index.html')


# Sign Up

def signup(request):
    return render(request, 'signup.html')


#Sign In


def signin(request):
    return render(request, 'signin.html')

def compra(request):
    return render(request, 'compra.html')

def carrito(request):
    ListadoCartas = Carta.objects.all()
    ctx = {'listado':ListadoCartas}
    return render(request,'carrito.html',ctx)

#CARRIT0

ConejilloIndias = Carta.objects.filter(id__icontains="1")
ConejilloIndias.update(nombre="Charizard")

ListadoCartas = Carta.objects.filter(nombre__contains='p')
ctx = {'protagonista':Carta, 'listado':ListadoCartas}


# INSERTAR REGISTROS:
def create(request, nuevoUsuario):
    usuarioNuevo = Usuario(nombre=nuevoUsuario)
    usuarioNuevo.save()
    return redirect(compra)

def delete(request, nuevoUsuario):
    personajeBorrar = Usuario.objects.filter(id__icontains=nuevoUsuario)
    personajeBorrar.delete()
    return redirect(compra)


def update(request, idUsuario,nuevoNombre):
    personajeActualizar = Usuario.objects.filter(id__icontains=idUsuario)
    personajeActualizar.update(nombre = nuevoNombre)
    return redirect(compra)