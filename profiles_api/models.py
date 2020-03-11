from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError("User must have an email")
        email=self.normalize_email(email)
        user=self.model(email=emal,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        """Create superuser using details"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=true
        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Datbase model for user in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retriver full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive Short name of user"""
        return self.name

    def __str__(self):
        """Return String representation of our user"""
        return self.email
