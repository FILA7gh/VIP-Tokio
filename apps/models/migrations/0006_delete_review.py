# Generated by Django 4.2.2 on 2023-07-10 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_alter_model_age_alter_model_height_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]