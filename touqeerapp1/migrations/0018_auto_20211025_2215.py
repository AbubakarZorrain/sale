# Generated by Django 3.1.4 on 2021-10-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touqeerapp1', '0017_auto_20211025_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ManyToManyField(to='touqeerapp1.Product'),
        ),
    ]
