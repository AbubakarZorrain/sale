# Generated by Django 3.1.4 on 2021-10-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touqeerapp1', '0007_auto_20211016_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pur',
            name='product',
            field=models.ManyToManyField(to='touqeerapp1.Product'),
        ),
    ]
