from typing import Any, Dict

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from slot_booking_backend.company.models import Company


class CustomUserManager(BaseUserManager):

    def create_user(self, email: str, **extra_fields: Dict[str, Any]):
        """
        Create and return a regular user with an email (no password as OTP authentication).
        """

        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, **extra_fields):
        """
        Create and return a superuser with an email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, **extra_fields)


class CustomUser(AbstractBaseUser):
    """

    """

    USER_TYPE_CHOICES = [
        ('interviewer', 'Interviewer'),
        ('interviewee', 'Interviewee'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'user_type']

    def __str__(self):
        return self.email
