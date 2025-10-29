from django.shortcuts import render

def hello_user(request, username):
    # 'render()' is a shortcut function in Django that combines three steps:
    #
    # 1️ Load a template:
    #    It finds the template file (e.g., 'index.html') in your templates directories.
    #
    # 2️ Create a Context:
    #    It takes the dictionary we pass (e.g., {'name': username}) and makes it
    #    available to the template as variables. Here, {{ name }} in the template
    #    will be replaced by the value of username.
    #
    # 3️ Return an HttpResponse:
    #    The template is rendered to a string (HTML content), and an HttpResponse
    #    object is returned with that HTML as the body. This response is sent
    #    back to the client (browser) to display.
    return render(request, 'index.html', {'name': username})
