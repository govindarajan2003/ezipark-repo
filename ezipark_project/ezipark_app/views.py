from django.shortcuts import render, redirect
from .models import  client, LandOwner, ParkingSlot
from django.contrib.auth import authenticate , login
from .forms import clientRegistrationForm,LandOwnerRegistrationForm
from django.contrib.auth.models import Group
# Create your views here.

def home(request):
    available_slots = ParkingSlot.objects.filter(available=True)
    return render(request, 'ezipark_app/home.html',{'available_slots': available_slots})

def search(request):
    pincode=request.GET.get('pincode', '')
    search_results = ParkingSlot.objects.filter(pincode=pincode, available=True)
    return render(request,'ezipark_app/search.html',{'search_results':search_results})

def login_view(request):
    message =None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = 'invalid username or password'
            
    return render(request, 'registration/login.html', {'message':message})

def client_registration(request):
    if request.method =='POST':
        form = clientRegistrationForm(request.POST)
        if form.is_valid():
            user= form.save( commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            client_group , created = Group.objects.get_or_create(name = 'client')
            client_group.user_set.add(user)

            client.objects.create(user= user)
            return redirect('home')
    else:
        form = clientRegistrationForm()
    return render(request, 'registration/client_registration.html',{'form':form})

def LandOwner_registration(request):
    if request.method=='POST':
        form = LandOwnerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            landowner_group , created = Group.objects.get_or_create(name='landowner')
            landowner_group.user_set.add(user)
            LandOwner.objects.create(user=user)
            return redirect('home')
    else:
        form = LandOwnerRegistrationForm()
    return render(request, 'registration/landOwner_registration.html',{'form':form})