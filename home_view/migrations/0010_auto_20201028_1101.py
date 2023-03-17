# Generated by Django 2.0.7 on 2020-10-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_view', '0009_auto_20201028_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=100)),
                ('unumber', models.CharField(max_length=100)),
                ('uorganisationname', models.CharField(max_length=100)),
                ('uemailaddress', models.CharField(max_length=100)),
                ('uaddress', models.CharField(max_length=100)),
                ('productid', models.CharField(max_length=100)),
                ('productcode', models.CharField(max_length=100)),
                ('productqty', models.CharField(max_length=100)),
                ('productamount', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('aname', models.CharField(max_length=100)),
                ('anumber', models.CharField(max_length=100)),
                ('bname', models.CharField(max_length=100)),
                ('transactionid', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='order_4',
        ),
    ]
