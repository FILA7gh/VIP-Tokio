# Generated by Django 4.2.3 on 2023-07-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0010_alter_model_package_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='country',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Ош', 'Ош')], default=False, max_length=100, verbose_name='Город'),
        ),
    ]
