# Generated by Django 2.2 on 2019-10-12 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='phone_length',
            field=models.CharField(max_length=100),
        ),
    ]
