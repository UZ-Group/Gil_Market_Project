# Generated by Django 3.1.7 on 2021-06-22 18:06

import Gil_Sliders.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('link', models.URLField(blank=True, max_length=150, null=True, verbose_name='آدرس')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Gil_Sliders.models.upload_image_path, verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'پست تبلیغی',
                'verbose_name_plural': 'پست های تبلیغی',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('link', models.URLField(max_length=150, verbose_name='آدرس')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Gil_Sliders.models.upload_image_path, verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدرها',
            },
        ),
    ]
