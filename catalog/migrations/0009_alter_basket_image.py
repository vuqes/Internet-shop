# Generated by Django 4.1.2 on 2022-11-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_basket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='image',
            field=models.ImageField(blank=True, upload_to='basket/%Y/%m/%d'),
        ),
    ]
