from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def home(request):
    books = Book.objects.all()  # SELECT * FROM BOOK
    context = {
        'books' : books
    }

    return render(request , 'index.html' , context)

def about(request):
    return render(request , 'about.html')
