# Generated by Django 4.2.2 on 2023-07-11 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_remove_additionalservice_title_and_more'),
        ('models', '0006_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='additional_service',
        ),
        migrations.AlterField(
            model_name='model',
            name='age',
            field=models.PositiveIntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='model',
            name='appearance',
            field=models.CharField(choices=[('Азиатская', 'aзиатская'), ('Европейская', 'европейская'), ('Экзотика', 'экзотика')], max_length=20, verbose_name='Внешность'),
        ),
        migrations.AlterField(
            model_name='model',
            name='area',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Район'),
        ),
        migrations.RemoveField(
            model_name='model',
            name='basic_service',
        ),
        migrations.AlterField(
            model_name='model',
            name='breast',
            field=models.CharField(choices=[('0-1', '0-1'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4+', '4+')], max_length=20, verbose_name='Размер груди'),
        ),
        migrations.AlterField(
            model_name='model',
            name='description',
            field=models.TextField(verbose_name='О себе и услугах'),
        ),
        migrations.RemoveField(
            model_name='model',
            name='extreme',
        ),
        migrations.AlterField(
            model_name='model',
            name='eyes',
            field=models.CharField(choices=[('Карие', 'карие'), ('Черные', 'черные'), ('Зеленые', 'зеленые'), ('Голубые', 'голубые'), ('Серые', 'серые')], max_length=20, verbose_name='Глаза'),
        ),
        migrations.AlterField(
            model_name='model',
            name='hairs',
            field=models.CharField(choices=[('Брюнетка', 'брюнетка'), ('Блондинка', 'блондинка'), ('Шатенка', 'шатенка'), ('Рыжие', 'рыжие'), ('Мелированные', 'мелированные')], max_length=20, verbose_name='Цвет волос'),
        ),
        migrations.AlterField(
            model_name='model',
            name='height',
            field=models.PositiveIntegerField(verbose_name='Рост (см)'),
        ),
        migrations.AlterField(
            model_name='model',
            name='in_osh',
            field=models.BooleanField(default=False, verbose_name='В оше'),
        ),
        migrations.AlterField(
            model_name='model',
            name='is_trans',
            field=models.BooleanField(default=False, verbose_name='Я транс'),
        ),
        migrations.RemoveField(
            model_name='model',
            name='massage',
        ),
        migrations.AlterField(
            model_name='model',
            name='nickname',
            field=models.CharField(max_length=100, verbose_name='Имя в анкете'),
        ),
        migrations.AlterField(
            model_name='model',
            name='package_price',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='services.packageprice', verbose_name='Выезд, апартаменты'),
        ),
        migrations.AlterField(
            model_name='model',
            name='phone_number',
            field=models.CharField(max_length=16, verbose_name='Телефон'),
        ),
        migrations.RemoveField(
            model_name='model',
            name='sadomazo',
        ),
        migrations.AlterField(
            model_name='model',
            name='schedule',
            field=models.CharField(max_length=19, verbose_name='Рабочее время'),
        ),
        migrations.AlterField(
            model_name='model',
            name='speak_english',
            field=models.BooleanField(default=False, verbose_name='I speak English'),
        ),
        migrations.RemoveField(
            model_name='model',
            name='striptease',
        ),
        migrations.AlterField(
            model_name='model',
            name='type',
            field=models.CharField(choices=[('Индивидуалка', 'индивидуалка'), ('Салон', 'салон')], max_length=20, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='model',
            name='weight',
            field=models.PositiveIntegerField(verbose_name='Вес'),
        ),
        migrations.AddField(
            model_name='model',
            name='additional_service',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='services.additionalservice', verbose_name='Дополнительные услуги'),
        ),
        migrations.AddField(
            model_name='model',
            name='basic_service',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='services.basicservice', verbose_name='Основные услуги'),
        ),
        migrations.AddField(
            model_name='model',
            name='extreme',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='services.extreme', verbose_name='Экстрим'),
        ),
        migrations.AddField(
            model_name='model',
            name='massage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='services.massage', verbose_name='Массаж'),
        ),
        migrations.AddField(
            model_name='model',
            name='sadomazo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='services.sadomazo', verbose_name='Садо-мазо'),
        ),
        migrations.AddField(
            model_name='model',
            name='striptease',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='services.striptease', verbose_name='Стриптиз'),
        ),
    ]
