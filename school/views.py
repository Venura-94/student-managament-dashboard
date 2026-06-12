from django.shortcuts import render


# ---------------------------------------------------------------------------
# Dashboards
# ---------------------------------------------------------------------------

def dashboard_admin(request):
    return render(request, "dashboard/admin.html")


def dashboard_teacher(request):
    return render(request, "dashboard/teacher.html")


def dashboard_student(request):
    return render(request, "dashboard/student.html")


# ---------------------------------------------------------------------------
# Students
# ---------------------------------------------------------------------------

def student_view(request):
    return render(request, "students/view.html")


def student_edit(request):
    return render(request, "students/edit.html")


# ---------------------------------------------------------------------------
# Teachers
# ---------------------------------------------------------------------------

def teacher_list(request):
    return render(request, "teachers/list.html", {"teachers": []})


def teacher_view(request):
    return render(request, "teachers/view.html")


def teacher_add(request):
    return render(request, "teachers/add.html")


def teacher_edit(request):
    return render(request, "teachers/edit.html")


# ---------------------------------------------------------------------------
# Departments & Subjects
# ---------------------------------------------------------------------------

def department_list(request):
    return render(request, "departments/list.html", {"departments": []})


def department_add(request):
    return render(request, "departments/add.html")


def subject_list(request):
    return render(request, "subjects/list.html", {"subjects": []})


def subject_add(request):
    return render(request, "subjects/add.html")


# ---------------------------------------------------------------------------
# Accounts
# ---------------------------------------------------------------------------

def fees_collection(request):
    return render(request, "accounts/fees_collection.html", {"fees": []})


def expenses(request):
    return render(request, "accounts/expenses.html", {"expenses": []})


def salary(request):
    return render(request, "accounts/salary.html", {"salaries": []})


def add_fees(request):
    return render(request, "accounts/add_fees.html")


def add_expenses(request):
    return render(request, "accounts/add_expenses.html")


def add_salary(request):
    return render(request, "accounts/add_salary.html")


# ---------------------------------------------------------------------------
# Holiday, Fees structure, Exam list, Events, Time Table, Library
# ---------------------------------------------------------------------------

def holiday(request):
    return render(request, "holiday/list.html", {"holidays": []})


def fees(request):
    return render(request, "fees/list.html", {"fees_structure": []})


def exam_list(request):
    return render(request, "exam/list.html", {"exams": []})


def events(request):
    return render(request, "events/list.html", {"events": []})


def timetable(request):
    return render(request, "timetable/list.html", {"periods": [], "timetable": []})


def library(request):
    return render(request, "library/list.html", {"books": []})


# ---------------------------------------------------------------------------
# Authentication, Blank page, Sports
# ---------------------------------------------------------------------------

def login(request):
    return render(request, "auth/login.html")


def register(request):
    return render(request, "auth/register.html")


def forgot_password(request):
    return render(request, "auth/forgot_password.html")


def blank_page(request):
    return render(request, "Home/blank.html")


def sports(request):
    return render(request, "sports/list.html", {"sports": []})
