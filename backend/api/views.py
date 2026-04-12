from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, NoteSerializer
from .models import Note
# Create your views here.

# Think of everything that your model can do or can be done to a model: add user, delete user
# Create a note, edit a note, all those logic will be written here
# Check if User age>30, then do something...all the app logic goes here.


# using function based view is also possible but class based view is more convenient and less code to write, it also provides more functionality out of the box like validation, authentication, etc.


# USE DOC TO KNOW WHAT METHODS BELONGS TO THE SPECIFIC CLASS
class NoteListCreate(generics.ListCreateAPIView):
    # This view will List already created notes or will create a new one
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # This gets the current user that is interacting with this route
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

# This view deletes the user note...self.request.user


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # This gets the current user that is interacting with this route
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # this allows anyone to access this view, even if they are not authenticated, because we want to allow anyone to register a new user
    permission_classes = [AllowAny]
