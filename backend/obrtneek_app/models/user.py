from django.contrib.auth.models import AbstractUser
from django.db import models

from obrtneek_app.managers import CustomUserManager
from obrtneek_app.models.company import Company


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        # Make sure only superusers can be without a company
        if not self.is_superuser and not self.company:
            raise ValueError("Regular users must have a company")

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email

    @property
    def full_name(self) -> str:
        # If the user has both first and last name, return them capitalized
        if self.first_name and self.last_name:
            return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

        # Default to email
        return self.email
