from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        addmission_number = request.POST.get('addmission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')

        #handling parent data
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_email = request.POST.get('mother_email')
        mother_mobile = request.POST.get('mother_mobile')
        mother_occupation = request.POST.get('mother_occupation')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        # save parent information
        parent = Parent.objects.create(
            father_name=father_name,
            father_occupation=father_occupation,
            father_mobile=father_mobile,
            father_email=father_email,
            mother_name=mother_name,
            mother_email=mother_email,
            mother_mobile=mother_mobile,
            mother_occupation=mother_occupation,
            present_address=present_address,
            permanent_address=permanent_address
        )

        # save student information
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            gender=gender,
            date_of_birth=date_of_birth,
            student_class=student_class,
            religion=religion,
            joining_date=joining_date,
            mobile_number=mobile_number,
            addmission_number=addmission_number,
            section=section,
            student_image=student_image,
            parent=parent
        )

        messages.success(request, 'Student added successfully!')
        return redirect('student_list')

    return render(request, 'students/add.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def edit_student(request):
    return render(request, 'students/edit.html') 

def view_student(request):
    return render(request, 'students/view.html')