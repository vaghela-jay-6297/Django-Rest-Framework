from django.urls import path
from .views import BookList_Create, Book_Update_delete
urlpatterns = [
    path('api/book', BookList_Create.as_view()),   # create generic class based view to create and get data.
    path('api/books/<int:pk>', Book_Update_delete.as_view()), # update,delete,retrive data and pass int id 
]