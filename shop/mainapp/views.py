import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    basket = get_basket(request.user)
    context = {
        'head_title': 'главная',
        'products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request, pk=None):
    categories_link = Category.objects.all()
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'Все'}
        else:
            category = get_object_or_404(Category, pk=pk)
            products = Product.objects.filter(category_name__pk=pk).order_by('price')
        context = {
            'head_title': 'каталог',
            'products': products,
            'categories_link': categories_link,
            'category': category,
            'basket': basket,
            'hot_product': hot_product,
            'same_products': same_products,

        }
        return render(request, 'mainapp/catalog.html', context)
    context = {
        'head_title': 'каталог',
        'same_products': same_products,
        'categories_link': categories_link,
        'hot_product':  hot_product,
        'basket': basket,

    }
    return render(request, 'mainapp/catalog.html', context)


def contact(request):
    basket = get_basket(request.user)
    context = {
        'head_title': 'контакты',
        'basket': basket,
    }
    return render(request, 'mainapp/contacts.html', context)


def card(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    basket = get_basket(request.user)
    context = {
        'head_title': 'продукт',
        'product': product,
        'basket': basket,
    }
    return render(request, 'mainapp/card_product.html', context)
# Create your views here.


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category_name=hot_product.category_name).exclude(pk=hot_product.pk)[:3]

    return same_products
