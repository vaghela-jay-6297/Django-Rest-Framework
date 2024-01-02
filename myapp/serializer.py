from rest_framework import serializers  # import serializers modual
from .models import Book    # import Book model

class BookSerializer(serializers.ModelSerializer):  # create BookSerializer class inheriting ModelSerializer class.
    class Meta:
        model=Book  # assign model class
        fields = ('id', 'author', 'isbn', 'publisher')  # select which field that shows to user side.