# Generated by Django 4.2.2 on 2023-06-26 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConfirmationCode',
        ),
    ]
