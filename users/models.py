from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy, reverse
# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, null=False, blank=False)
    username = models.CharField(unique=True, max_length=256, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=256, null=False, blank=False)
    password_1 = models.CharField(max_length=256, null=False, blank=False)
    password_2 = models.CharField(max_length=256, null=False, blank=False)
    registration_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"username: {self.username}, email: {self.email}"


    # def get_absolute_url(self):
    #     return reverse_lazy("profile", kwargs={"username": self.username})

