# Generated by Django 3.2 on 2021-05-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gil_Products', '0009_auto_20210505_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='مبلغ تخفیف'),
        ),
    ]
