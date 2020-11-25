# Generated by Django 2.1.7 on 2020-06-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_cartitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='size',
            field=models.CharField(default='N/A', max_length=10),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='topping1',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='topping2',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='topping3',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='topping4',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='topping5',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
