from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Finch, Habitat
from .forms import FeedingForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.habitats.all().values_list('id')
    habitat_finch_doesnt_have = Habitat.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)



class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 's_name', 'origin', 'description']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 's_name', 'origin', 'description']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class HabitatList(ListView):
    model = Habitat

class HabitatDetail(DetailView):
    model = Habitat

class HabitatCreate(CreateView):
    model = Habitat
    fields = '__all__'
class HabitatUpdate(UpdateView):
    model = Habitat
    fields = ['name', 'description']

class HabitatDelete(DeleteView):
    model = Habitat
    success_url = '/habitats'