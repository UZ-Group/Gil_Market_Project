# Generated by Django 3.1.7 on 2021-06-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_user_account', '0002_auto_20210622_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=True, verbose_name='سوپر ادمین'),
        ),
    ]
