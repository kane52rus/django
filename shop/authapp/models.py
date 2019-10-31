from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):
    user_photo = models.ImageField(upload_to='users_photo', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

# Create your models here.
