# Generated by Django 4.2.2 on 2023-07-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_remove_model_additional_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='in_osh',
        ),
        migrations.AddField(
            model_name='model',
            name='country',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош')], default=False, max_length=50, verbose_name='Город'),
        ),
    ]
