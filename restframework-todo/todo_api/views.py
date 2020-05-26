from django.shortcuts import render

from rest_framework import viewsets

from todo_api import serializers
from todo_api import models
from todo_api import permissions


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

    permission_classes = (permissions.UpdateOwnProfile,)
