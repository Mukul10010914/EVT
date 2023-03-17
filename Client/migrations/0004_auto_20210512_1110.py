# Generated by Django 2.1.15 on 2021-05-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=11),
        ),
        migrations.AddField(
            model_name='profile',
            name='oname',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]