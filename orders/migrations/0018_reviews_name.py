# Generated by Django 3.1.3 on 2020-11-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
