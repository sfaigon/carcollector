from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Accessory
from .forms import OilChangeForm

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {
        'cars': cars
    })
def cars_details(request, car_id):
    car = Car.objects.get(id=car_id)
    id_list = car.accessories.all().values_list('id')
    accessories_car_doesnt_have = Accessory.objects.exclude(id__in=id_list)
    oilchange_form = OilChangeForm()
    return render(request, 'cars/detail.html', {
        'car': car,
        "oilchange_form": oilchange_form,
        "accessories": accessories_car_doesnt_have
    })
class CarCreate(CreateView):
    model = Car 
    fields = ["name","make", "model", "year", "color", "description"]
    success_url = "/cars"
class CarUpdate(UpdateView):
    model = Car
    fields = ["make", "model", "year", "color", "description"]
class CarDelete(DeleteView):
    model = Car
    success_url = "/cars"
def add_oilchange(request, car_id):
  form = OilChangeForm(request.POST)
  if form.is_valid():
    new_oilchange = form.save(commit=False)
    new_oilchange.car_id = car_id
    new_oilchange.save()
  return redirect('detail', car_id=car_id)
class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory
class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color', 'description']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories'

def assoc_accessory(request, car_id, accessory_id):
  Car.objects.get(id=car_id).accessories.add(accessory_id)
  return redirect("detail", car_id=car_id)

def unassoc_accessory(request, car_id, accessory_id):
  Car.objects.get(id=car_id).accessories.remove(accessory_id)
  return redirect("detail", car_id=car_id)
