# Generated by Django 4.1.2 on 2022-11-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_account_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, upload_to='users_photo/%Y/%m/%d'),
        ),
    ]