from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Candidate(models.Model):
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Age must be between 0 and 100.",
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
