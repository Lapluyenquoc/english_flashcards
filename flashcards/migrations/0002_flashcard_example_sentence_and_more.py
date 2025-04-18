# Generated by Django 5.2 on 2025-04-05 21:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='example_sentence',
            field=models.TextField(blank=True, null=True, verbose_name='Пример предложения (английский)'),
        ),
        migrations.AddConstraint(
            model_name='deck',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='unique_deck_name_per_user'),
        ),
    ]
