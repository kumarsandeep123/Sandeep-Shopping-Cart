# Generated by Django 4.0 on 2021-12-21 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handsome', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
