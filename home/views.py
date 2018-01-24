from django.shortcuts import render, redirect

#from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from home.models import Place
from home.forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

'''class PlaceCreate(CreateView):
    model = Place
    fields = ['nombre_propietario', 'nombre_local', 'typo']

class PlaceUpdate(UpdateView):
    model = Place
    fields = ['nombre_propietario', 'nombre_local', 'typo']

class PlaceDelete(DeleteView):
    model = Place
    success_url = redirect('datos')'''

class PlacesListView(ListView):
    model = Place
    template_name = 'datos.html'

class PlaceDetailView(DetailView):
    model = Place
    template_name = 'detalle.html'

    '''def get_context_data(self, *args, **kwargs):
        context = super(PlaceDetailView, self).get_context_data(*args, **kwargs)
        return context'''

def home(request):
    context={
        'nombre': 'Andres',
        'apellido': 'Caicedo'
    }
    return render(request, 'index.html', context)

def nosotros(request):
    context={}
    return render(request, 'nosotros.html', context)

def gracias(request):
    context={}
    return render(request, 'gracias.html', context)

def contactenos(request):
    if request.method == 'POST':
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            correo = formulario.cleaned_data['correo']
            mensaje = formulario.cleaned_data['mensaje']
            body_message = "Nombre: " + nombre.upper() + "\n" + "Correo: " + correo + "\n" + "Mensaje: " + mensaje
            send_mail('Mensaje de la aplicacion galerias', body_message, 'cmauricio10@gmail.com', ['amcaicedo@unimayor.edu.co'])
            return redirect('gracias')
    else:
        formulario = ContactForm()
    context={
        'form': formulario
    }
    return render(request, 'contactenos.html', context)