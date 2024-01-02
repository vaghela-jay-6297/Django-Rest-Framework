from django.shortcuts import render
from rest_framework import generics # import generics modual 
from .models import Book
from.serializer import BookSerializer

# Create your views here.
class BookList_Create(generics.ListCreateAPIView):  # get data & create object in table using ListCreateAPIView.
    queryset = Book.objects.all()   # get all object of Book model
    serializer_class = BookSerializer   # to create object in table using BookSerializer
    
# retrieve single data, update, delete object using RetrieveDestroyAPIView
class Book_Update_delete(generics.RetrieveDestroyAPIView): 
    queryset = Book
    serializer_class = BookSerializer