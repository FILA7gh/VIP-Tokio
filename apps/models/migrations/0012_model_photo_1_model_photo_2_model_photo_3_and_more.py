# Generated by Django 4.2.3 on 2023-07-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0011_alter_model_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='photo_1',
            field=models.ImageField(null=True, upload_to='model_photos'),
        ),
        migrations.AddField(
            model_name='model',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='model_photos'),
        ),
        migrations.AddField(
            model_name='model',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='model_photos'),
        ),
        migrations.AddField(
            model_name='model',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='model_photos'),
        ),
        migrations.AddField(
            model_name='model',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to='model_photos'),
        ),
        migrations.AddField(
            model_name='model',
            name='photo_6',
            field=models.ImageField(blank=True, null=True, upload_to='model_photos'),
        ),
        migrations.AddField(
            model_name='model',
            name='photo_7',
            field=models.ImageField(blank=True, null=True, upload_to='model_photos'),
        ),
        migrations.DeleteModel(
            name='ModelsGallery',
        ),
    ]
