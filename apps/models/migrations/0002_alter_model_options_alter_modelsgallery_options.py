# Generated by Django 4.2 on 2023-06-23 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model',
            options={'verbose_name': 'Модель', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AlterModelOptions(
            name='modelsgallery',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереи'},
        ),
    ]
