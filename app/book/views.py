from django.shortcuts import render, redirect
from app.book.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from app.book.models import Book
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     else:
#         form = UserRegisterForm()
#     return render(request, "registration/register.html", {'form':form})

# @login_required
# def book(request):
#     books = Book.objects.all()
#     return render(request, "book/book.html", locals())

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'books'