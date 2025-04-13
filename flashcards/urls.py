from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    home,
    DeckListView,
    DeckDetailView,
    FlashcardCreateView,
    FlashcardUpdateView,
    FlashcardDeleteView,
    register,
    CustomLoginView,
    CustomLogoutView,
    StudyView,
    DeckCreateView,
    DeckDeleteView,
)

urlpatterns = [
    path('decks/<int:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('decks/<int:deck_id>/add/', FlashcardCreateView.as_view(), name='flashcard-create'),
    path('flashcards/<int:pk>/edit/', FlashcardUpdateView.as_view(), name='flashcard-update'),
    path('flashcards/<int:pk>/delete/', FlashcardDeleteView.as_view(), name='flashcard-delete'),
    path('register/', register, name='register'),
    path('decks/', DeckListView.as_view(), name='deck-list'),
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('decks/<int:pk>/study/', StudyView.as_view(), name='deck-study'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('decks/create/', DeckCreateView.as_view(), name='deck-create'),
    path('decks/<int:pk>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
]
