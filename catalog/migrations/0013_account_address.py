# Generated by Django 4.1.2 on 2022-11-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_account_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
