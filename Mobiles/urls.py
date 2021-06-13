from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('covid', views.index, name='index'),
    path('sale', views.sale, name='sale'),
    path('grocery',views.grocery , name='grocery'),


]   