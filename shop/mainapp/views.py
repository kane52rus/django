from django.shortcuts import render


def index(request):
    hit = [
        {
            'item_name': 'Мэтт Вайсфельд. Объектно-ориентированное мышление',
            'item_link': '/catalog/card1.html',
            'item_img_link': 'img/book1.jpg',
        },
        {
            'item_name': 'Бертран Мейер. Почувствуй класс',
            'item_link': '/catalog/card2.html',
            'item_img_link': 'img/book2.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
    ]
    context = {
        'head_title': 'главная',
        'hit': hit
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    catalog = [
        {
            'item_name': 'Мэтт Вайсфельд. Объектно-ориентированное мышление',
            'item_link': '/catalog/card1.html',
            'item_img_link': 'img/book1.jpg',
        },
        {
            'item_name': 'Бертран Мейер. Почувствуй класс',
            'item_link': '/catalog/card2.html',
            'item_img_link': 'img/book2.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
        {
            'item_name': 'Гради Буч. Объектно-ориентированный анализ и проектирование с примерами приложений',
            'item_link': '/catalog/card3.html',
            'item_img_link': 'img/book3.jpg',
        },
    ]
    context = {
        'head_title': 'каталог',
        'catalog': catalog,
    }
    return render(request, 'mainapp/catalog.html', context)


def contact(request):
    context = {
        'head_title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', context)
# Create your views here.
