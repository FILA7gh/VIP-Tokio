# Generated by Django 4.2.2 on 2023-07-17 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_delete_basicservicebool'),
        ('models', '0009_remove_model_in_osh_model_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='package_price',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='model', to='services.packageprice', verbose_name='Выезд, апартаменты'),
        ),
    ]