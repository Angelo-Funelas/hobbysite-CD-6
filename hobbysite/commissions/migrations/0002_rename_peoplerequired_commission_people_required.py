# Generated by Django 5.1.7 on 2025-03-09 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commission',
            old_name='peopleRequired',
            new_name='people_required',
        ),
    ]
