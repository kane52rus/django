from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()

    context = {
        'head_title': 'главная',
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    products = Product.objects.all()
    context = {
        'head_title': 'каталог',
        'products': products,
    }
    return render(request, 'mainapp/catalog.html', context)


def contact(request):
    context = {
        'head_title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', context)
# Create your views here.
