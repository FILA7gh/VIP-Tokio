# Generated by Django 4.2.3 on 2023-07-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_basicservice_boolean_alter_basicservice_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicservice',
            name='boolean',
        ),
        migrations.AlterField(
            model_name='basicservice',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Основная услуга'),
        ),
    ]
