# Generated by Django 3.1.4 on 2021-10-16 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touqeerapp1', '0004_auto_20211016_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='rate',
        ),
    ]
