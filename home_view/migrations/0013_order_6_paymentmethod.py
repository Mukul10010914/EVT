# Generated by Django 2.1.15 on 2021-05-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_view', '0012_auto_20201202_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_6',
            name='paymentmethod',
            field=models.CharField(default='Payment On Delivery', max_length=100),
        ),
    ]
