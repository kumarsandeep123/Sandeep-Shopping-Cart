# Generated by Django 4.0 on 2021-12-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handsome', '0006_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
