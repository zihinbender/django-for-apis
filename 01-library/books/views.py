from django.views.generic import ListView

from .models import Book

class BookList(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"


