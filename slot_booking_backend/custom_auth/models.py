from typing import Any, Dict

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email: str, password: str, **extra_fields: Dict[str, Any]):
        """
        Create and return a regular user with an email and password.
        """

        if not email:
            raise ValueError('The email field must be set')
        if not password:
            raise ValueError('The password filed must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        """
        Create and return a superuser with an email and password
        Args:
            email:
            password:
            **extra_fields:

        Returns: creates a superuser

        """


class CustomUser(AbstractBaseUser):
    """

    """

    USER_TYPE_CHOICES = [
        ('interviewer', 'Interviewer'),
        ('interviewee', 'Interviewee'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES)
    company = models.CharField(max_length=255, blank=True, null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'user_type']

    def __str__(self):
        return self.email
