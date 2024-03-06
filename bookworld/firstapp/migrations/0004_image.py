# Generated by Django 4.2.6 on 2024-03-06 10:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_alter_person_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание изображения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Файл с изображением')),
            ],
            managers=[
                ('obj_img', django.db.models.manager.Manager()),
            ],
        ),
    ]
