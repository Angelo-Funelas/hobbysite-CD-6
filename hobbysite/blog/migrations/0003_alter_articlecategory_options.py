# Generated by Django 4.2.19 on 2025-05-12 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_author_article_header_image_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name'], 'verbose_name': 'Article category', 'verbose_name_plural': 'Article categories'},
        ),
    ]
