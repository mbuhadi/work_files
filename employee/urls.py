from django.urls import path
from django.conf import settings
from employee import views

urlpatterns = [
    path("employee", views.EmployeeListCreate.as_view()),
]