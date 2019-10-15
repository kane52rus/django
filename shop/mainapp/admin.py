from django.contrib import admin
from .models import Product, Category, Authors

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Authors)
# Register your models here.
