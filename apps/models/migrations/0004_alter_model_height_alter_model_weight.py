# Generated by Django 4.2 on 2023-06-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_alter_model_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='weight',
            field=models.PositiveIntegerField(null=True),
        ),
    ]