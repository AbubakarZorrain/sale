# Generated by Django 3.1.4 on 2021-10-16 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('touqeerapp1', '0005_auto_20211016_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('quantity', models.IntegerField(null=True)),
                ('scheme', models.IntegerField(null=True)),
                ('discountPercent', models.IntegerField(null=True)),
                ('discount', models.IntegerField(null=True)),
                ('gst', models.IntegerField(null=True)),
                ('value', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='touqeerapp1.company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='touqeerapp1.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
