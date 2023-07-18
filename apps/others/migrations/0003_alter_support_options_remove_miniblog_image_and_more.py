# Generated by Django 4.2.2 on 2023-07-14 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0002_didyouknow_help_alter_support_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='support',
            options={'verbose_name': 'Техподдержка', 'verbose_name_plural': 'Техподдержка'},
        ),
        migrations.RemoveField(
            model_name='miniblog',
            name='image',
        ),
        migrations.CreateModel(
            name='MiniBlogGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='MiniBlog')),
                ('mini_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mini_blog', to='others.miniblog')),
            ],
        ),
    ]