# Generated by Django 3.1.4 on 2021-10-16 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touqeerapp1', '0003_auto_20211016_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseitem',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='discountPercent',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='gst',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='scheme',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='value',
        ),
    ]
