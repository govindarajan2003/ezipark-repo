from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home ,name ='home'),
    path('search/', views.search, name='search'),
    path('login/', views.login_view , name ='login'),
    path('signup/client', views.client_registration, name='client_registration'),
    path('signup/landowner', views.LandOwner_registration , name ='LandOwner_registration'),
]