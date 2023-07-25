from apps.services.models import *
from django.db import models
from djongo import models as mongo
from django.contrib.auth.models import User


class Model(models.Model):
    CHOICE_APPEARANCE = (('Азиатская', 'aзиатская'), ('Европейская', 'европейская'), ('Экзотика', 'экзотика'))
    CHOICE_EYES = (('Карие', 'карие'), ('Черные', 'черные'), ('Зеленые', 'зеленые'),
                   ('Голубые', 'голубые'), ('Серые', 'серые'))
    CHOICE_HAIRS = (('Брюнетка', 'брюнетка'), ('Блондинка', 'блондинка'),
                    ('Шатенка', 'шатенка'), ('Рыжие', 'рыжие'), ('Мелированные', 'мелированные'))
    CHOICE_TYPE = (('Индивидуалка', 'индивидуалка'), ('Салон', 'салон'))
    CHOICE_BREAST = (('0-1', '0-1'), ('1', '1'), ('1.5', '1.5'),
                     ('2', '2'), ('2.5', '2.5'), ('3', '3'),
                     ('3.5', '3.5'), ('4', '4'), ('4+', '4+'))
    CHOICE_COUNTRY = (('Бишкек', 'Бишкек'), ('Ош', 'Ош'))

    # models
    nickname = models.CharField(max_length=100, verbose_name='Имя в анкете')
    description = models.TextField(verbose_name='О себе и услугах')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    appearance = models.CharField(choices=CHOICE_APPEARANCE, max_length=20, verbose_name='Внешность')
    height = models.PositiveIntegerField(verbose_name='Рост (см)')
    weight = models.PositiveIntegerField(verbose_name='Вес')
    eyes = models.CharField(choices=CHOICE_EYES, max_length=20, verbose_name='Глаза')
    hairs = models.CharField(choices=CHOICE_HAIRS, max_length=20, verbose_name='Цвет волос')
    type = models.CharField(choices=CHOICE_TYPE, max_length=20, verbose_name='Тип')
    area = models.CharField(max_length=100, null=True, blank=True, verbose_name='Район')
    breast = models.CharField(choices=CHOICE_BREAST, max_length=20, verbose_name='Размер груди')
    phone_number = models.CharField(max_length=16, verbose_name='Телефон')
    schedule = models.CharField(max_length=19, verbose_name='Рабочее время')
    speak_english = models.BooleanField(default=False, verbose_name='I speak English')
    is_trans = models.BooleanField(default=False, verbose_name='Я транс')
    country = models.CharField(choices=CHOICE_COUNTRY, default=False, verbose_name='Город', max_length=100)

    photo_1 = models.ImageField(upload_to='model_photos', null=True)
    photo_2 = models.ImageField(upload_to='model_photos', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='model_photos', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='model_photos', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='model_photos', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='model_photos', blank=True, null=True)
    photo_7 = models.ImageField(upload_to='model_photos', blank=True, null=True)

    # services
    package_price = models.OneToOneField(PackagePrice, on_delete=models.PROTECT, related_name='model',
                                         verbose_name='Выезд, апартаменты', null=True)

    basic_service = models.ManyToManyField(BasicService, related_name='model',
                                           verbose_name='Основные услуги')

    additional_service = models.ManyToManyField(AdditionalService, related_name='model',
                                                blank=True, verbose_name='Дополнительные услуги')

    massage = models.ManyToManyField(Massage, related_name='model',
                                     blank=True, verbose_name='Массаж')

    striptease = models.ManyToManyField(Striptease, related_name='model',
                                        blank=True, verbose_name='Стриптиз')

    sadomazo = models.ManyToManyField(SadoMazo, related_name='model',
                                      blank=True, verbose_name='Садо-мазо')

    extreme = models.ManyToManyField(Extreme, related_name='model',
                                     blank=True, verbose_name='Экстрим')

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Review(mongo.Model):
    username = models.CharField(max_length=50, verbose_name='Никнейм')
    text = models.CharField(max_length=255, verbose_name='Сообщение')
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.model}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
