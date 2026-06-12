from django.shortcuts import render

# Create your views here.
def add_student(request):
    return render(request, 'students/add.html')

def student_list(request):
    return render(request, 'students/list.html')

def edit_student(request):
    return render(request, 'students/edit.html') 

def view_student(request):
    return render(request, 'students/view.html')