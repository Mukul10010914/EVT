# Generated by Django 2.1.15 on 2021-05-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0005_delete_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
