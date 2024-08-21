from django.db import models

MAX_LENGTH = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Maker(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Toys(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.FloatField(verbose_name='Размер(см.)')
    material = models.CharField(max_length=MAX_LENGTH, verbose_name='Материал')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступен к заказу')

    category = models.ManyToManyField(Category, blank=True, null=True, verbose_name='Категория')
    maker = models.ForeignKey(Maker, on_delete=models.PROTECT, verbose_name='Производитель')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = 'Игрушка'
        verbose_name_plural = 'Игрушки'


class Order(models.Model):
    SHOP = 'SH'
    COURIER = 'CR'
    TYPE_DELIVERY = [
        (SHOP, 'Самовывоз'),
        (COURIER, 'Курьер'),
    ]
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя заказчика')
    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия заказчика')
    delivery_address = models.CharField(null=True, blank=True, max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ получения')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    finish = models.BooleanField(default=False, verbose_name='Выполнен?')

    toys = models.ManyToManyField(Toys, through=, verbose_name='Игрушка')

    def __str__(self):
        return f"№{self.pk} - ({self.buyer_name} {self.buyer_firstname}) ({self.create_date})"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
