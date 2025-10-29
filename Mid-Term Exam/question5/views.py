from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentapp/student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the student to the database
            return redirect('student_list')  # Redirect to list after saving
    else:
        form = StudentForm()

    return render(request, 'studentapp/add_student.html', {'form': form})
