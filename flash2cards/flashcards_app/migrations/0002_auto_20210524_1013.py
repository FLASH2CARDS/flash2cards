# Generated by Django 3.2.3 on 2021-05-24 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flashcard',
            options={'ordering': ['modification_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='flashcardset',
            options={'ordering': ['modification_date']},
        ),
    ]
