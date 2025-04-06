from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Flashcard, Deck
from .forms import FlashcardForm, RegistrationForm

# Tạo thẻ mới
class FlashcardCreateView(CreateView):
    model = Flashcard
    form_class = FlashcardForm
    template_name = 'flashcards/flashcard_form.html'

    def form_valid(self, form):
        # Gán deck từ URL và user hiện tại
        form.instance.deck_id = self.kwargs['deck_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('deck-detail', kwargs={'pk': self.kwargs['deck_id']})

# Cập nhật thẻ
class FlashcardUpdateView(UpdateView):
    model = Flashcard
    form_class = FlashcardForm
    template_name = 'flashcards/flashcard_form.html'

    def get_success_url(self):
        return reverse_lazy('deck-detail', kwargs={'pk': self.object.deck_id})

# Xóa thẻ
class FlashcardDeleteView(DeleteView):
    model = Flashcard
    template_name = 'flashcards/flashcard_confirm_delete.html'


from django.views.generic import DetailView

class DeckDetailView(DetailView):
    model = Deck
    template_name = 'flashcards/deck_detail.html'
    context_object_name = 'deck'

    def get_queryset(self):
        return Deck.objects.filter(user=self.request.user)

# flashcards/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'flashcards/home.html')

# flashcards/views.py
from django.views.generic import ListView
from .models import Deck

class DeckListView(ListView):
    model = Deck
    template_name = 'flashcards/deck_list.html'
    context_object_name = 'decks'

    def get_queryset(self):
        # Hiển thị deck theo user đăng nhập
        return Deck.objects.filter(user=self.request.user)
# flashcards/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm  # Đảm bảo đã tạo form này

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Đăng nhập tự động sau khi đăng ký
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'flashcards/register.html', {'form': form})
# flashcards/views.py
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'flashcards/login.html'
    redirect_authenticated_user = True  # Chuyển hướng nếu đã đăng nhập
# flashcards/views.py
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = 'home'  # Trang chuyển hướng sau khi đăng xuất
# flashcards/views.py
from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Deck, Flashcard

class StudyView(DetailView):
    model = Deck
    template_name = 'flashcards/study.html'
    context_object_name = 'deck'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flashcards'] = self.object.flashcards.all()
        return context

# flashcards/views.py
from django.views.generic.edit import CreateView
from .models import Deck
from .forms import DeckForm

class DeckCreateView(CreateView):
    model = Deck
    form_class = DeckForm
    template_name = 'flashcards/deck_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Truyền user vào form
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user  # Gán user cho deck
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('deck-list')

# flashcards/views.py
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Deck

class DeckDeleteView(DeleteView):
    model = Deck
    template_name = 'flashcards/deck_confirm_delete.html'
    success_url = reverse_lazy('deck-list')

    def get_queryset(self):
        # Chỉ cho phép xóa deck của chính user
        return Deck.objects.filter(user=self.request.user)
