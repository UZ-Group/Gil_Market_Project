# Generated by Django 3.2 on 2021-05-04 18:26

import Gil_Products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gil_Product_Brand', '0001_initial'),
        ('Gil_Products_Category', '0002_auto_20210429_1351'),
        ('Gil_Products', '0007_product_brands'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Gil_Products.models.upload_gallery_path, verbose_name='تصویر')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gil_Product_Brand.productbrand', verbose_name='برند')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gil_Products_Category.productcategory', verbose_name='دسته بندی')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gil_Products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
    ]