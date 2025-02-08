from django.urls import path
from app.book.views import BookListView, RegisterView

urlpatterns = [
    # path("register/", register, name='register'),
    # path("", book, name='book')
    path("", BookListView.as_view(), name='book_list'),
    path("register/", RegisterView.as_view(), name='register')
]