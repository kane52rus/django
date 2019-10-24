from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, Category


def index(request):
    products = Product.objects.all()

    context = {
        'head_title': 'главная',
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request, pk=None):
    categories_link = Category.objects.all()
    basket = []
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
        }
        return render(request, 'mainapp/catalog.html', context)
    same_products = Product.objects.all()[3:5]
    context = {
        'head_title': 'каталог',
        'same_products': same_products,
        'categories_link': categories_link,
    }
    return render(request, 'mainapp/catalog.html', context)


def contact(request):
    context = {
        'head_title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', context)


def card(request, pk=None):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'head_title': 'продукт',
        'product': product,
    }
    return render(request, 'mainapp/card_product.html', context)
# Create your views here.
