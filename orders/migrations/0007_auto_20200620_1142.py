# Generated by Django 2.1.7 on 2020-06-20 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200620_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(choices=[('Cheese', 'Cheese'), ('1 Topping', '1 Topping'), ('2 Toppings', '2 Toppings'), ('3 Toppings', '3 Toppings'), ('Special', 'Special')], max_length=64),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='pizza_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='orders.Category'),
        ),
    ]
