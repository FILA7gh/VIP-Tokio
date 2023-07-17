from django.db import models


class BasicService(models.Model):
    title = models.CharField(max_length=50, verbose_name='Основная услуга', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Основная услуга'
        verbose_name_plural = 'Основные услуги'


# class BasicServiceBool(models.Model):
#     CHOICES = (('Yes', 'Да'), ('No', 'Нет'))
#
#     boolean = models.CharField(choices=CHOICES, max_length=20, null=True)


class AdditionalService(models.Model):
    title = models.CharField(max_length=50, verbose_name='Доп услуга', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'


class Massage(models.Model):
    title = models.CharField(max_length=50, verbose_name='Массаж', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Массаж'
        verbose_name_plural = 'Массажи'


class Striptease(models.Model):
    title = models.CharField(max_length=50, verbose_name='Стриптиз', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Стриптиз'
        verbose_name_plural = 'Стриптизы'


class SadoMazo(models.Model):
    title = models.CharField(max_length=50, verbose_name='Садо Мазо', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Садо Мазо'
        verbose_name_plural = 'Садо Мазо'


class Extreme(models.Model):
    title = models.CharField(max_length=50, verbose_name='Экстрим', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Экстрим'
        verbose_name_plural = 'Экстримы'


class PackagePrice(models.Model):
    apartments_1h = models.PositiveIntegerField(blank=True, default=0, verbose_name='Апартаменты 1 час')
    apartments_2h = models.PositiveIntegerField(blank=True, default=0, verbose_name='Апартаменты 2 часа')
    apartments_night = models.PositiveIntegerField(blank=True, default=0, verbose_name='Апартаменты ночь')
    departure_1h = models.PositiveIntegerField(blank=True, default=0, verbose_name='Выезд 1 час')
    departure_2h = models.PositiveIntegerField(blank=True, default=0, verbose_name='Выезд 2 часа')
    departure_night = models.PositiveIntegerField(blank=True, default=0, verbose_name='Выезд ночь')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Пакет цен'
        verbose_name_plural = ' Пакеты цен'
