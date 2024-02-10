from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=128)
    image = models.ImageField(default="default_profile.jpg", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"username: {self.username}, email: {self.email}"


    class Meta:
        db_table = "Custom user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    

