# Generated by Django 3.1.3 on 2020-11-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_reviews_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]