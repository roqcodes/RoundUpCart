from typing import ContextManager
from django.forms import fields
from Mobiles.forms import Payment
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    # sale = Saled.objects.all()
    form = Payment()
    if request.method == 'POST':
        form = Payment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'index.html', {'products': products , 'form':form})
    # Context = {
    #     'title':'trigger'
    # }
    # return HttpResponse('<h1>Welcome to django project</h1>')
def grocery(request):
    products = Product.objects.all()
    form = Payment()
    filter = Product.name
    if request.method == 'POST':
        form = Payment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grocery')
    return render(request,'grocery.html',{'products':products ,'form':form})

def sale(request):
    products = Product.objects.all()
    # return HttpResponse('<h1>Welcome to sale</h1>')
    return render(request, 'sale.html', {'products': products})

# def button_function(request,value):
