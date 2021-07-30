from django.urls import path
from . import views


urlpatterns = [
    path('<str:name>', views.index, name='index'),
    #<str:name>
    path('', views.home, name='home'),
    path('About/', views.about, name='about'),
]