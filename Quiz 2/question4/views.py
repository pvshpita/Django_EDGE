from django.shortcuts import render

def hello_user(request, username):
    return render(request, 'index.html', {'name': username})
