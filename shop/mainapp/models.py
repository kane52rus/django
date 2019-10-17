from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        verbose_name='Наименование категории',
        max_length=64,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )

    def __str__(self):
        return self.category_name


class Authors(models.Model):
    author_name = models.CharField(
        verbose_name='Автор',
        max_length=128
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True
    )

    def __str__(self):
        return self.author_name


class Product(models.Model):
    product_name = models.CharField(
        verbose_name='Наименование продукта',
        max_length=128
    )
    category_name = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    author_name = models.ForeignKey(
        Authors,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        blank=True,
        max_length=240
    )
    serial = models.TextField(
        verbose_name='Серия',
        blank=True
    )
    language = models.TextField(
        verbose_name='Язык издания',
        blank=True
    )
    type = models.TextField(
        verbose_name='Тип',
        blank=True
    )
    issue_year = models.IntegerField(
        verbose_name='Год выпуска',
        blank=True
    )
    price = models.DecimalField(
        verbose_name='Цена продукта',
        max_digits=7,
        decimal_places=2,
        default=0
    )
    balance = models.IntegerField(
        verbose_name='Остаток на складе',
        default=0
    )
    product_image = models.ImageField(
        upload_to='products_images',
        blank=True
    )

    def __str__(self):
        return f"{self.author_name.author_name}. {self.product_name} ({self.category_name.category_name})"
