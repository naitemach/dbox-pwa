from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('patient', views.patient, name='patient'),
    path('test', views.test, name='test' ),
    path('searchpat', views.searchpat, name='searchpat' ),
    path('addpat', views.addpat, name='addpat' ),


]