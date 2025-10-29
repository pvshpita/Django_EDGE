from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)        # Student's name
    roll = models.CharField(max_length=20, unique=True)  # Roll number (unique)
    department = models.CharField(max_length=50)   # Department name
    email = models.EmailField(unique=True)         # Email address (unique)

    def __str__(self):
        return f"{self.name} ({self.roll})"
