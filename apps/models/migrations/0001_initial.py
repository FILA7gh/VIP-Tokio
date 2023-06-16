# Generated by Django 4.2 on 2023-06-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='model_photo')),
                ('description', models.TextField()),
                ('nickname', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('appearance', models.IntegerField(choices=[('aзиатская', 'aзиатская'), ('европейская', 'европейская'), ('экзотика', 'экзотика')])),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('eyes', models.IntegerField(choices=[('карие', 'карие'), ('черные', 'черные'), ('зеленые', 'зеленые'), ('голубые', 'голубые'), ('серые', 'серые')])),
                ('hairs', models.IntegerField(choices=[('брюнетка', 'брюнетка'), ('блондинка', 'блондинка'), ('шатенка', 'шатенка'), ('рыжие', 'рыжие'), ('мелированные', 'мелированные')])),
                ('type', models.IntegerField(choices=[('Индивидуалка', 'Индивидуалка'), ('Салон', 'Салон')])),
                ('area', models.CharField(max_length=100)),
                ('breast', models.IntegerField(choices=[('0-1', '0-1'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4+', '4+')])),
                ('phone_number', models.CharField(max_length=16)),
                ('schedule', models.CharField(max_length=19)),
                ('speak_english', models.BooleanField(default=False)),
                ('is_trans', models.BooleanField(default=False)),
                ('in_osh', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
    ]
