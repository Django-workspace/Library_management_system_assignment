from django.db import models
from account.models import User
from books.models import books
# Create your models here.

class borrow_book(models.Model):
    borrower = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)
    book = models.ForeignKey(books, max_length=100, on_delete=models.CASCADE)
    borrowed = models.BooleanField(default=False)
    borrowed_on = models.DateField(auto_now_add=True)
    retrieve_on = models.DateField()
    fine = models.BooleanField(default=False)
    
    
    

    