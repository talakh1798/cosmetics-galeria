# Generated by Django 2.2.4 on 2024-08-03 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmatics_app', '0002_remove_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
