from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from todo_api import serializers
from todo_api import models
from todo_api import permissions


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

    permission_classes = (permissions.UpdateOwnProfile,)
    authentication_classes = (TokenAuthentication,)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class TodoItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating todo items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.TodoItemSerializer
    queryset = models.TodoItem.objects.all()

    permission_classes = (permissions.UpdateOwnTodo,)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user=self.request.user)


class AuthInfoGetView(generics.RetrieveAPIView):
    """Retrieve the logged in user information"""
