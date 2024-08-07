# Generated by Django 2.2.4 on 2024-08-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmatics_app', '0005_product_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='cosmatics_app.User'),
        ),
    ]
