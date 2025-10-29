from django.contrib import admin
from .models import Student

# Register Student model so it appears in Django Admin
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'department', 'email')
