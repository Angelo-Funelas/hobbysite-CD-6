# Generated by Django 4.2.16 on 2025-05-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0006_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='merchstore/product_images/'),
        ),
    ]
