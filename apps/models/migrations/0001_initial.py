<<<<<<< HEAD
# Generated by Django 4.2 on 2023-06-17 17:11
=======
# Generated by Django 4.2 on 2023-06-17 18:58
>>>>>>> a07991d3042f7ce76052cb199ae89a8f7ac863e3

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('services', '0001_initial'),
=======
>>>>>>> a07991d3042f7ce76052cb199ae89a8f7ac863e3
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
                ('appearance', models.CharField(choices=[('Азиатская', 'aзиатская'), ('Европейская', 'европейская'), ('Экзотика', 'экзотика')], max_length=20)),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('eyes', models.CharField(choices=[('Карие', 'карие'), ('Черные', 'черные'), ('Зеленые', 'зеленые'), ('Голубые', 'голубые'), ('Серые', 'серые')], max_length=20)),
                ('hairs', models.CharField(choices=[('Брюнетка', 'брюнетка'), ('Блондинка', 'блондинка'), ('Шатенка', 'шатенка'), ('Рыжие', 'рыжие'), ('Мелированные', 'мелированные')], max_length=20)),
                ('type', models.CharField(choices=[('Индивидуалка', 'индивидуалка'), ('Салон', 'салон')], max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('breast', models.CharField(choices=[('0-1', '0-1'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4+', '4+')], max_length=20)),
                ('phone_number', models.CharField(max_length=16)),
                ('schedule', models.CharField(max_length=19)),
                ('speak_english', models.BooleanField(default=False)),
                ('is_trans', models.BooleanField(default=False)),
                ('in_osh', models.BooleanField(default=False)),
<<<<<<< HEAD
                ('additional_service', models.ManyToManyField(to='services.additionalservice')),
                ('basic_service', models.ManyToManyField(to='services.basicservice')),
                ('extreme', models.ManyToManyField(to='services.extreme')),
                ('massage', models.ManyToManyField(to='services.massage')),
                ('sadomazo', models.ManyToManyField(to='services.sadomazo')),
                ('striptease', models.ManyToManyField(to='services.striptease')),
=======
>>>>>>> a07991d3042f7ce76052cb199ae89a8f7ac863e3
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
    ]
