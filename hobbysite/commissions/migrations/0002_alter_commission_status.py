# Generated by Django 4.2.19 on 2025-05-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('full', 'Full'), ('completed', 'Completed'), ('discontinued', 'Discontinued')], max_length=20),
        ),
    ]
