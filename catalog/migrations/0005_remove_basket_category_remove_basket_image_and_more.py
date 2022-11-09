# Generated by Django 4.1.2 on 2022-11-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_basket_user_account_basket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='category',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='image',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='stock',
        ),
        migrations.AlterField(
            model_name='basket',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
