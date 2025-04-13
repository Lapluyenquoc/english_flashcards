# flashcards/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Deck(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название колоды")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_deck_name_per_user')
        ]

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, related_name='flashcards', on_delete=models.CASCADE, verbose_name="Колода")
    front = models.TextField(verbose_name="Передняя сторона (русский)")  
    back = models.TextField(verbose_name="Задняя сторона (английский)")   
    created_at = models.DateTimeField(auto_now_add=True)
    example_sentence = models.TextField(  
        verbose_name="Пример предложения (английский)",
        blank=True, null=True  
    )
    def __str__(self):
        return f"{self.front} → {self.back}"

