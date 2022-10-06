from django.db import models

class Book(models.Model):
    

    name = models.CharField(max_length = 200, default = "Default") #"name" variable that has maximum capacity of characters of 200.

    authors = models.JSONField() # "authors" stores data in dictionaries,lists,strings,numbers,booleans or None.

    year_published = models.IntegerField #Accepts integers from -2147483648 to 2147483647

    date_added = models.DateTimeField(auto_now_add = True) # sets the time of when object is created

    date_modified = models.DateTimeField(auto_now = True) # sets the current time,  everytime object is saved

    def __str__(self):

        return self.name #returns string representation of the model

    
class Review (models.Model):

    my_review = models.TextField() #creates a text field to input the review
    
    stars = models.IntegerField() #represents an integer value

    unfinished = models.BooleanField(default = False) # a boolean value

    date_added = models.DateTimeField(auto_now_add = True) #sets the time of when object is created

    date_modified = models.DateTimeField(auto_now = True) #sets the current time, everytime object is saved

    book = models.ForeignKey(Book,on_delete = models.CASCADE) # sets foreign key that connects to the  book model.

    def __str__(self):  # Returns string representation of the model

        return f"{self.my_review}..."