"""Defines URL patterns for crazy_book_clubs."""

from django.urls import path
from . import views
app_name = 'crazy_books_clubs'
urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),
    #Books page
    path('books/', views.books, name = 'books'),
    path('reviews/<int:book_id>/', views.reviews, name = 'reviews'),
]