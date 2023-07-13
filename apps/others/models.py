from django.db import models


class DidYouKnow(models.Model):
    answer = models.CharField(max_length=100, verbose_name='вопрос', null=True)
    question = models.TextField(verbose_name='ответ', null=True)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'А знаете ли вы?'
        verbose_name_plural = 'А знаете ли вы?'


class Help(models.Model):
    answer = models.CharField(max_length=100, verbose_name='вопрос', null=True)
    question = models.TextField(verbose_name='ответ', null=True)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = 'Помощь'


class Support(models.Model):  # Техподдержка
    name = models.CharField(max_length=20, unique=True, verbose_name='Имя', null=True)
    mail = models.EmailField(max_length=50, unique=True, verbose_name='E-mail', null=True)
    subject = models.CharField(max_length=20, verbose_name='Тема', null=True)
    message = models.TextField(verbose_name='Сообщение', null=True)

    def __str__(self):
        return f'User: {self.name}, Subject: {self.subject}'

    class Meta:
        verbose_name = 'Техподдержка'
        verbose_name_plural = 'Техподдержка'


class MiniBlog(models.Model):  # Мини блог
    title = models.CharField(max_length=100, verbose_name='Название', null=True)
    image = models.ImageField(verbose_name='Фотография', blank=True, null=True)
    text = models.TextField(verbose_name='Текст', null=True)
    # user = models.ForeignKey('User', verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мини блог'
        verbose_name_plural = 'Мини блог'


class AboutUs(models.Model):  # О нас
    title = models.CharField(max_length=100, verbose_name='Название', null=True)
    text = models.TextField(verbose_name='Текст', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
