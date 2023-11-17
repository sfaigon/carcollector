from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
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
    oilchange_form = OilChangeForm()
    return render(request, 'cars/detail.html', {
        'car': car,
        "oilchange_form": oilchange_form
    })
class CarCreate(CreateView):
    model = Car 
    fields = "__all__"
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
