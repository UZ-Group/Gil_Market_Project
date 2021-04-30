# Generated by Django 3.2 on 2021-04-30 06:21

import Gil_Products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fa', models.CharField(max_length=30, verbose_name='نام محصول (فارسی)')),
                ('name_en', models.CharField(max_length=50, verbose_name='نام محصول (انگلیسی)')),
                ('year', models.IntegerField(verbose_name='سال تولید')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='مبلغ تخفیف')),
                ('description', models.TextField(verbose_name='توضیحات محصول')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Gil_Products.models.upload_image_path, verbose_name='تصویر')),
                ('active', models.BooleanField(default=False, verbose_name='موجود / ناموجود')),
            ],
        ),
    ]