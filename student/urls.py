"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.student_list, name="student_list"),
    path("add/",views.add_student, name="add_student"),
    path("view/<slug:slug>/",views.view_student, name="view_student"),
    path("edit/<slug:slug>/",views.edit_student, name="edit_student"),
    path("delete/<slug:slug>/",views.delete_student, name="delete_student"),
]
