# Generated by Django 2.0.7 on 2020-10-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]
