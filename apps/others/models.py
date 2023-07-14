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
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя', null=True)
    mail = models.EmailField(max_length=100, unique=True, verbose_name='E-mail', null=True)
    subject = models.CharField(max_length=100, verbose_name='Тема', null=True)
    message = models.TextField(verbose_name='Сообщение', null=True)

    def __str__(self):
        return f'User: {self.name}, Subject: {self.subject}'

    class Meta:
        verbose_name = 'Техподдержка'
        verbose_name_plural = 'Техподдержка'


class MiniBlog(models.Model):  # Мини блог
    title = models.CharField(max_length=100, verbose_name='Название', null=True)
    text = models.TextField(verbose_name='Текст', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мини блог'
        verbose_name_plural = 'Мини блог'


class MiniBlogGallery(models.Model):
    photo = models.ImageField(upload_to='MiniBlog', blank=True)
    mini_blog = models.ForeignKey(MiniBlog, on_delete=models.CASCADE, related_name='gallery')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class AboutUs(models.Model):  # О нас
    title = models.CharField(max_length=100, verbose_name='Название', null=True)
    text = models.TextField(verbose_name='Текст', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Rules(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Правила'
        verbose_name_plural = 'Правила'


class Contact(models.Model):
    phone_number_1 = models.CharField(max_length=16, verbose_name='номер телефона')
    phone_number_2 = models.CharField(max_length=16, blank=True, verbose_name='номер телефона')
    phone_number_3 = models.CharField(max_length=16, blank=True, verbose_name='номер телефона')
    social_media_1 = models.URLField(verbose_name='соц сеть')
    social_media_2 = models.URLField(blank=True, verbose_name='соц сеть')
    social_media_3 = models.URLField(blank=True, verbose_name='соц сеть')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
