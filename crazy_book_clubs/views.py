from django.shortcuts import render
from .models import Book
from .models import Review
# Create your views here.

def index(request):
    '''The home page for crazy_books_club.'''
    return render(request, 'crazy_book_clubs/index.html')

def books(request):
    '''Shows all books.'''
    all_books = Book.objects.all()
    book_dict = {'books': all_books}
    return render(request, 'crazy_book_clubs/books.html', book_dict)

def reviews(request, book_id):
    '''Displays review for a particular book'''
    book = Book.objects.get(id = book_id)
    reviews = Review.objects.filter(book = book_id)
    reviews_dict = {'book': book, 'review': reviews}
    return render(request, 'crazy_book_clubs/reviews.html', reviews_dict)
