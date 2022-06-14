from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index, name='home'),
    path('about-us',views.about, name='about'),
    path('our_dog',views.our_dog, name='our_dog'),
    path('puppy',views.puppy, name='puppy'),
    path('create', views.create, name='create'),
    path('pometbeagle', views.pometbeagle, name='pometbeagle'),
    path('pometkorgi', views.pometkorgi, name='pometkorgi'),
    path('register/', views.register, name="register"),
    path('login/', views.LoginPase, name="login"),
    path('logout/', views.logout, name="logout"),
]
