# Generated by Django 3.1.5 on 2021-02-08 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfbuy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketdetail',
            name='quantity',
        ),
    ]
