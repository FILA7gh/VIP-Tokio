# Generated by Django 4.2.2 on 2023-07-17 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_remove_additionalservice_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicServiceBool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.CharField(choices=[('Yes', 'Да'), ('No', 'Нет')], max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='additionalservice',
            name='cum_in_mouth',
        ),
        migrations.RemoveField(
            model_name='additionalservice',
            name='cum_on_face',
        ),
        migrations.RemoveField(
            model_name='additionalservice',
            name='deep_blowjob',
        ),
        migrations.RemoveField(
            model_name='additionalservice',
            name='escort',
        ),
        migrations.RemoveField(
            model_name='additionalservice',
            name='photo_video_shooting',
        ),
        migrations.RemoveField(
            model_name='additionalservice',
            name='role_playing_games',
        ),
        migrations.RemoveField(
            model_name='additionalservice',
            name='services_for_couples',
        ),
        migrations.RemoveField(
            model_name='additionalservice',
            name='toys',
        ),
        migrations.RemoveField(
            model_name='basicservice',
            name='anal_sex',
        ),
        migrations.RemoveField(
            model_name='basicservice',
            name='blowjob_without_condom',
        ),
        migrations.RemoveField(
            model_name='basicservice',
            name='classic_sex',
        ),
        migrations.RemoveField(
            model_name='basicservice',
            name='condom_blowjob',
        ),
        migrations.RemoveField(
            model_name='basicservice',
            name='cunnilingus',
        ),
        migrations.RemoveField(
            model_name='basicservice',
            name='group_sex',
        ),
        migrations.RemoveField(
            model_name='basicservice',
            name='lesbian_sex',
        ),
        migrations.RemoveField(
            model_name='extreme',
            name='anilingus',
        ),
        migrations.RemoveField(
            model_name='extreme',
            name='fisting_anal',
        ),
        migrations.RemoveField(
            model_name='extreme',
            name='fisting_vaginal',
        ),
        migrations.RemoveField(
            model_name='extreme',
            name='golden_rain_issuance',
        ),
        migrations.RemoveField(
            model_name='extreme',
            name='golden_rain_reception',
        ),
        migrations.RemoveField(
            model_name='extreme',
            name='strapon',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='classic_massage',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='erotic_massage',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='pro_massage',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='prostate_massage',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='relaxing_massage',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='sakura_branch',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='thai_massage',
        ),
        migrations.RemoveField(
            model_name='sadomazo',
            name='bandage',
        ),
        migrations.RemoveField(
            model_name='sadomazo',
            name='fetish',
        ),
        migrations.RemoveField(
            model_name='sadomazo',
            name='flogging',
        ),
        migrations.RemoveField(
            model_name='sadomazo',
            name='light_domination',
        ),
        migrations.RemoveField(
            model_name='sadomazo',
            name='mistress',
        ),
        migrations.RemoveField(
            model_name='sadomazo',
            name='slave',
        ),
        migrations.RemoveField(
            model_name='sadomazo',
            name='trampling',
        ),
        migrations.RemoveField(
            model_name='striptease',
            name='candid_lesbian_show',
        ),
        migrations.RemoveField(
            model_name='striptease',
            name='easy_lesbian_show',
        ),
        migrations.RemoveField(
            model_name='striptease',
            name='striptease_not_pro',
        ),
        migrations.RemoveField(
            model_name='striptease',
            name='striptease_pro',
        ),
        migrations.AddField(
            model_name='additionalservice',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Доп услуга'),
        ),
        migrations.AddField(
            model_name='basicservice',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Основная услуга'),
        ),
        migrations.AddField(
            model_name='extreme',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Экстрим'),
        ),
        migrations.AddField(
            model_name='massage',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Массаж'),
        ),
        migrations.AddField(
            model_name='sadomazo',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Садо Мазо'),
        ),
        migrations.AddField(
            model_name='striptease',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Стриптиз'),
        ),
    ]
