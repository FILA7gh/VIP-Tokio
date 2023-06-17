from django.db import models


class Support(models.Model):  # Техподдержка
    name = models.CharField('Имя', max_length=20, unique=True)
    mail = models.EmailField('Почта', max_length=50, unique=True)
    subject = models.CharField('Тема', max_length=20)
    message = models.TextField('Сообщение')

    def __str__(self):
        return f'User: {self.name} Subject: {self.subject}'


class MiniBlog(models.Model):
    title = models.CharField('Название', max_length=30)
    image = models.ImageField('Фотография')
    description = models.TextField('Текст')

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    text = models.TextField('Текст')

    def __str__(self):
        return self.text.split()[:5]



