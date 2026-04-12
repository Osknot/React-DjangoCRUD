from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Normally all the models which represent the entirety of your webapp is defined here.


# Everything about the entities in your app is the model.
# The user, the notes...YOU DEFINE ALL THOSE THINGS HERE
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title
