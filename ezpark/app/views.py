from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def index(request):
    return render(request, "home.html")



def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def login(request):
   if request.method == "POST":
      username = request.POST['uname']
      password = request.POST['psw']
      usernamecheck = Member.objects.filter(firstname=username)
      passwordcheck = Member.objects.filter(password=password)
      if(usernamecheck.count() != 0 and passwordcheck.count()!=0):
         return render(request, "loginhome.html")
      else:
        return HttpResponse("not logged in")
      print(username)
   return render(request, "login.html")

def signup(request):
   temp= loader.get_template('reg.html')
   return HttpResponse(temp.render())