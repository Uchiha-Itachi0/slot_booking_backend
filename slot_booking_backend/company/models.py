from django.db import models


class Company(models.Model):
    """
    Model to represent a company.
    One company can have multiple users (interviewers).
    """
    name = models.CharField(max_length=255)
    address = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name
