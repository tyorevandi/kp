from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Message

class IndexMessage(ListView):
    queryset = Message.objects.all()

class TambahMessage(CreateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('page1:index')

class UpdateMessage(UpdateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('page1:index')

class HapusMessage(DeleteView):
    model = Message
    success_url = reverse_lazy('page1:index')