from apps.services.models import *
from django.db import models


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
    in_osh = models.BooleanField(default=False, verbose_name='В оше')

    # services
    package_price = models.OneToOneField(PackagePrice, on_delete=models.CASCADE, related_name='model',
                                         verbose_name='Выезд, апартаменты', null=True)

    basic_service = models.OneToOneField(BasicService, on_delete=models.CASCADE, related_name='model',
                                         verbose_name='Основные услуги', null=True)

    additional_service = models.OneToOneField(AdditionalService, on_delete=models.CASCADE, related_name='model',
                                              blank=True, verbose_name='Дополнительные услуги', null=True)

    massage = models.OneToOneField(Massage, on_delete=models.CASCADE, related_name='model',
                                   blank=True, verbose_name='Массаж', null=True)

    striptease = models.OneToOneField(Striptease, on_delete=models.CASCADE, related_name='model',
                                      blank=True, verbose_name='Стриптиз', null=True)

    sadomazo = models.OneToOneField(SadoMazo, on_delete=models.CASCADE, related_name='model',
                                    blank=True, verbose_name='Садо-мазо', null=True)

    extreme = models.OneToOneField(Extreme, on_delete=models.CASCADE, related_name='model',
                                   blank=True, verbose_name='Экстрим', null=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class ModelsGallery(models.Model):
    photo = models.ImageField(upload_to='model_photos')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='gallery')

    def __str__(self):
        return f'{self.model}'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

#
# class Review(models.Model):
#     username = models.CharField(max_length=20)
#     text = models.CharField(max_length=255)
#     model = models.ForeignKey(Model, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.model
