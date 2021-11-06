# Generated by Django 3.1.4 on 2021-10-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('quantity', models.IntegerField(null=True)),
                ('scheme', models.IntegerField(null=True)),
                ('rate', models.IntegerField(null=True)),
                ('discountPercent', models.IntegerField(null=True)),
                ('discount', models.IntegerField(null=True)),
                ('gst', models.IntegerField(null=True)),
                ('value', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_image/')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]