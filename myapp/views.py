from myapp.models import *
from myapp.forms import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

def index_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def catalog_page(request):
    charg = Door.objects.filter(material='Царговый')
    shtamp = Door.objects.filter(material='Штампованный')
    glass = Door.objects.filter(material='Стекло')
    if request.method == 'POST':
        if 'Delivery' in request.POST:
            form = Delivery(fullname=request.POST['fullname'], phone=request.POST['phone'], address=request.POST['address'], date=request.POST['date'])
            form.save()
            return redirect('catalog')
            pass
        
    return render(request, 'catalog.html', context={'charg': charg, 'shtamp': shtamp, 'glass': glass})

def in_page(request):
    return render(request, 'in.html')

def map_page(request):
    return render(request, 'map.html')

def login_page(request):
    return render(request, 'registration/login.html')

def account_page(request):
    if request.method == 'POST':
        if 'AddDoor' in request.POST:
            form = AddDoorForm(request.POST, request.FILES)  # Обновление аргументов
            if form.is_valid():
                door = form.save(commit=False)  # Создание экземпляра модели, но не сохранение его в базу данных
                door.save()  # Сохранение объекта в базу данных
                return redirect('account')

    else:
        form = AddDoorForm()

    return render(request, 'account.html', {'form': form})

class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')