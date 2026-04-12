# this is the default user model provided by django
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # these are the fiedls we want to return in response, there are part of the User model by django
        fields = ['id', 'username', 'password',]
        extra_kwargs = {
            # only write and donot return the password in response
            'password': {'write_only': True}
        }

    def create(self, validated_data):  # this method is called when we call serializer.save() in the view, it creates a new user with the validated data and returns the user object
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True}
        }
