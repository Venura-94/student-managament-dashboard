import re
from datetime import datetime
from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import get_object_or_404, render, redirect

from .models import *
from django.contrib import messages

NAME_PATTERN = re.compile(r'^[A-Za-z ]+$')
STUDENT_ID_PATTERN = re.compile(r'^[A-Za-z0-9\-]+$')
MOBILE_PATTERN = re.compile(r'^\d{10,15}$')
VALID_GENDERS = {'Male', 'Female'}
VALID_CLASSES = {'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII'}
VALID_SECTIONS = {'A', 'B', 'C', 'D'}


def _validate_student_form(request, current_student=None):
    first_name = request.POST.get('first_name', '').strip()
    last_name = request.POST.get('last_name', '').strip()
    student_id = request.POST.get('student_id', '').strip()
    gender = request.POST.get('gender', '').strip()
    date_of_birth = request.POST.get('date_of_birth', '').strip()
    student_class = request.POST.get('student_class', '').strip()
    religion = request.POST.get('religion', '').strip()
    joining_date = request.POST.get('joining_date', '').strip()
    mobile_number = request.POST.get('mobile_number', '').strip()
    addmission_number = request.POST.get('addmission_number', '').strip()
    section = request.POST.get('section', '').strip()
    student_image = request.FILES.get('student_image')

    #handling parent data
    father_name = request.POST.get('father_name', '').strip()
    father_occupation = request.POST.get('father_occupation', '').strip()
    father_mobile = request.POST.get('father_mobile', '').strip()
    father_email = request.POST.get('father_email', '').strip()
    mother_name = request.POST.get('mother_name', '').strip()
    mother_email = request.POST.get('mother_email', '').strip()
    mother_mobile = request.POST.get('mother_mobile', '').strip()
    mother_occupation = request.POST.get('mother_occupation', '').strip()
    present_address = request.POST.get('present_address', '').strip()
    permanent_address = request.POST.get('permanent_address', '').strip()

    errors = []

    # required fields
    required_fields = [
        ('First Name', first_name),
        ('Last Name', last_name),
        ('Student ID', student_id),
        ('Gender', gender),
        ('Date of Birth', date_of_birth),
        ('Religion', religion),
        ('Class', student_class),
        ('Section', section),
        ('Mobile Number', mobile_number),
        ('Admission Number', addmission_number),
        ('Joining Date', joining_date),
        ('Present Address', present_address),
        ('Permanent Address', permanent_address),
        ('Father Name', father_name),
        ('Father Occupation', father_occupation),
        ('Father Mobile', father_mobile),
        ('Father Email', father_email),
        ('Mother Name', mother_name),
        ('Mother Occupation', mother_occupation),
        ('Mother Mobile', mother_mobile),
        ('Mother Email', mother_email),
    ]
    for label, value in required_fields:
        if not value:
            errors.append(f"{label} is required.")

    if current_student is None and not student_image:
        errors.append("Profile Photo is required.")

    # format checks
    for label, value in [('First Name', first_name), ('Last Name', last_name), ('Religion', religion),
                          ('Father Name', father_name), ('Mother Name', mother_name)]:
        if value and not NAME_PATTERN.match(value):
            errors.append(f"{label} must contain letters only.")

    if student_id and not STUDENT_ID_PATTERN.match(student_id):
        errors.append("Student ID must contain only letters, numbers and hyphens.")

    for label, value in [('Mobile Number', mobile_number), ('Father Mobile', father_mobile),
                          ('Mother Mobile', mother_mobile)]:
        if value and not MOBILE_PATTERN.match(value):
            errors.append(f"{label} must be 10 to 15 digits.")

    for label, value in [('Father Email', father_email), ('Mother Email', mother_email)]:
        if value:
            try:
                validate_email(value)
            except ValidationError:
                errors.append(f"{label} is not a valid email address.")

    if gender and gender not in VALID_GENDERS:
        errors.append("Gender must be Male or Female.")

    if student_class and student_class not in VALID_CLASSES:
        errors.append("Class must be one of I-XII.")

    if section and section not in VALID_SECTIONS:
        errors.append("Section must be one of A-D.")

    addmission_number_value = None
    if addmission_number:
        try:
            addmission_number_value = Decimal(addmission_number)
            if addmission_number_value < 0:
                errors.append("Admission Number cannot be negative.")
        except InvalidOperation:
            errors.append("Admission Number must be a valid number.")

    date_of_birth_value = None
    if date_of_birth:
        try:
            date_of_birth_value = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        except ValueError:
            errors.append("Date of Birth must be a valid date.")

    joining_date_value = None
    if joining_date:
        try:
            joining_date_value = datetime.strptime(joining_date, '%Y-%m-%d').date()
        except ValueError:
            errors.append("Joining Date must be a valid date.")

    existing = Student.objects.filter(student_id=student_id)
    if current_student is not None:
        existing = existing.exclude(pk=current_student.pk)
    if student_id and existing.exists():
        errors.append("A student with this Student ID already exists.")

    parent_data = {
        'father_name': father_name,
        'father_occupation': father_occupation,
        'father_mobile': father_mobile,
        'father_email': father_email,
        'mother_name': mother_name,
        'mother_email': mother_email,
        'mother_mobile': mother_mobile,
        'mother_occupation': mother_occupation,
        'present_address': present_address,
        'permanent_address': permanent_address,
    }

    # used to re-populate the form if validation fails
    display_data = {
        'first_name': first_name,
        'last_name': last_name,
        'student_id': student_id,
        'addmission_number': addmission_number,
        'date_of_birth': date_of_birth_value,
        'gender': gender,
        'religion': religion,
        'student_class': student_class,
        'section': section,
        'mobile_number': mobile_number,
        'joining_date': joining_date_value,
        'parent': parent_data,
    }

    # used to save/update the records once validation passes
    clean_data = {
        'first_name': first_name,
        'last_name': last_name,
        'student_id': student_id,
        'gender': gender,
        'date_of_birth': date_of_birth_value,
        'student_class': student_class,
        'religion': religion,
        'joining_date': joining_date_value,
        'mobile_number': mobile_number,
        'addmission_number': addmission_number_value,
        'section': section,
        'student_image': student_image,
        'parent': parent_data,
    }

    return errors, display_data, clean_data


# Create your views here.
def add_student(request):
    if request.method == 'POST':
        errors, display_data, clean_data = _validate_student_form(request)

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'students/add.html', {'student': display_data})

        # save parent information
        parent = Parent.objects.create(**clean_data['parent'])

        # save student information
        Student.objects.create(
            first_name=clean_data['first_name'],
            last_name=clean_data['last_name'],
            student_id=clean_data['student_id'],
            gender=clean_data['gender'],
            date_of_birth=clean_data['date_of_birth'],
            student_class=clean_data['student_class'],
            religion=clean_data['religion'],
            joining_date=clean_data['joining_date'],
            mobile_number=clean_data['mobile_number'],
            addmission_number=clean_data['addmission_number'],
            section=clean_data['section'],
            student_image=clean_data['student_image'],
            parent=parent
        )

        messages.success(request, 'Student added successfully!')
        return redirect('student_list')

    return render(request, 'students/add.html')

def student_list(request):
    students_list = Student.objects.select_related('parent').all()
    context = {
        'students_list': students_list
    }
    return render(request, 'students/list.html', context)

def edit_student(request, slug):
    student = get_object_or_404(Student, slug=slug)

    if request.method == 'POST':
        errors, display_data, clean_data = _validate_student_form(request, current_student=student)

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'students/edit.html', {'student': display_data, 'is_edit': True})

        parent = student.parent
        for field, value in clean_data['parent'].items():
            setattr(parent, field, value)
        parent.save()

        for field in ['first_name', 'last_name', 'student_id', 'gender', 'date_of_birth', 'student_class',
                       'religion', 'joining_date', 'mobile_number', 'addmission_number', 'section']:
            setattr(student, field, clean_data[field])
        if clean_data['student_image']:
            student.student_image = clean_data['student_image']
        student.save()

        messages.success(request, 'Student updated successfully!')
        return redirect('view_student', slug=student.slug)

    return render(request, 'students/edit.html', {'student': student, 'is_edit': True})

def delete_student(request, slug):
    student = get_object_or_404(Student, slug=slug)

    if request.method == 'POST':
        parent = student.parent
        parent.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')

    return render(request, 'students/delete.html', {'student': student})

def view_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    context = {
        'student': student
    }
    return render(request, 'students/view.html', context)
