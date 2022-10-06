from django.contrib import admin

# Registering Book model
from.models import Book
admin.site.register(Book) 

# Registering Review model
from.models import Review
admin.site.register(Review)
