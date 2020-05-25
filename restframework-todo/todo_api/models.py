from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager for user"""

    def create_user(self, email, display_name, password=None):
        """Create a new user"""
        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, display_name=display_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, display_name, password):
        """Create and save a new superuser with given details"""

        user = self.create_user(email, display_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255)
    about = models.CharField(max_length=100)
    avatar_url = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']

    def __str__(self):
        return self.email
