from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView  # view
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona
"""

class listView():
  model = Persona
  template_name ='index.html'
  
  def dispatch()
  
  def get_contex_data(self):
        context={}
        context['queryset'] = self.get_queryset()
        return context
    
  def get_queryset(self):
        return self.model.objects.all()
    
  def get_templates_names():
        return self.templates_name

  def post()self,request,*args,**kwargs):
        return render(request,self.get_templates_names(),self.get_queryset())
"""
class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'



class PerconaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')