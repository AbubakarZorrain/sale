# Generated by Django 3.1.4 on 2021-10-25 13:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('touqeerapp1', '0010_auto_20211025_1853'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pur',
            new_name='Purchase',
        ),
    ]
