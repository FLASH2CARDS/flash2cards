# Generated by Django 3.2.3 on 2021-05-24 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards_app', '0002_auto_20210524_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
