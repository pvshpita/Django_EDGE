from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:username>/', views.hello_user, name='hello_user'),
]
