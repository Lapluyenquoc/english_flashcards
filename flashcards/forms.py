from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['front', 'back']
        labels = {
            'front': 'Передняя сторона (русский)',
            'back': 'Задняя сторона (английский)',
        }
        widgets = {
            'front': forms.Textarea(attrs={'rows': 2}),
            'back': forms.Textarea(attrs={'rows': 2}),
        }
# flashcards/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }

# flashcards/forms.py
from django import forms
from .models import Deck


# flashcards/forms.py
class DeckForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name']
        if self.user and Deck.objects.filter(user=self.user, name=name).exists():
            raise forms.ValidationError('Колода с таким названием уже существует!')
        return name

    class Meta:
        model = Deck
        fields = ['name']
        labels = {'name': 'Название колоды'}

# flashcards/forms.py
from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['front', 'back', 'example_sentence'] 
        labels = {
            'front': 'Передняя сторона (русский)',
            'back': 'Задняя сторона (английский)',
            'example_sentence': 'Пример предложения (английский)', 
        }
        widgets = {
            'front': forms.Textarea(attrs={'rows': 2}),
            'back': forms.Textarea(attrs={'rows': 2}),
            'example_sentence': forms.Textarea(attrs={'rows': 3}), 
        }
