from django.shortcuts import render
from .models import Student

def student_list(request):
    # Fetch all student records from the database
    students = Student.objects.all()

    # Pass them to the template for rendering
    return render(request, 'studentapp/student_list.html', {'students': students})
