# Generated by Django 3.1.4 on 2021-10-31 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touqeerapp1', '0023_auto_20211026_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='employee',
            field=models.ManyToManyField(to='touqeerapp1.Employee'),
        ),
    ]