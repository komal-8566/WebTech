# Generated by Django 2.1.7 on 2020-06-22 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200621_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='order_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
