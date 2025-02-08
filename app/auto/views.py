from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car
from .forms import CarForm


class CarListView(ListView):
    model = Car
    template_name = 'avto/car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'avto/car_detail.html'
    context_object_name = 'car'

# class CarCreateView(CreateView):
#     model = Car
#     form_class = CarForm
#     template_name = 'cars/car_form.html'
#     success_url = reverse_lazy('car_list')  

# class CarUpdateView(UpdateView):
#     model = Car
#     form_class = CarForm
#     template_name = 'cars/car_form.html'
#     context_object_name = 'car'
#     success_url = reverse_lazy('car_list')  


# class CarDeleteView(DeleteView):
#     model = Car
#     template_name = 'cars/car_confirm_delete.html'
#     context_object_name = 'car'
#     success_url = reverse_lazy('car_list')  
