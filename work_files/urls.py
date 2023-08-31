
from django.contrib import admin
from django.urls import path, include

COMMON_PATH = "api/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(COMMON_PATH + "employee/", include("employee.urls")),
]
