# Generated by Django 4.2.19 on 2025-05-12 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_articlecategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name'], 'verbose_name': 'Article Category', 'verbose_name_plural': 'Article Categories'},
        ),
    ]
