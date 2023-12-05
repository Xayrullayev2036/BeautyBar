from django.db import models


class CategoryTypeChoices(models.TextChoices):
    MALE = ("Erkak", "erkak")
    FAMALE = ("Ayol", "ayol")
