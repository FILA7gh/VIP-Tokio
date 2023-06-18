from django.db import models


class BasicService(models.Model):  # Основные услуги
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Основная услуга'
        verbose_name_plural = 'Основные услуги'


class AdditionalService(models.Model):  # Доп услуги
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'


class Massage(models.Model):  # Сообщение
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Массаж'
        verbose_name_plural = 'Массажи'


class Extreme(models.Model):  # Экстрим
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экстрим'
        verbose_name_plural = 'Экстримы'


class SadoMazo(models.Model):  # Садо Мазо
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Садо Мазо'
        verbose_name_plural = 'Садо Мазо'


class Striptease(models.Model):  # Стриптиз
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стриптиз'
        verbose_name_plural = 'Стриптизы'


