from django.urls import path
from school import views

urlpatterns = [
    # Dashboards
    path('', views.dashboard_admin, name="dashboard_admin"),
    path('teacher-dashboard/', views.dashboard_teacher, name="dashboard_teacher"),
    path('student-dashboard/', views.dashboard_student, name="dashboard_student"),

    # Students
    path('student/view/', views.student_view, name="student_view"),
    path('student/edit/', views.student_edit, name="student_edit"),

    # Teachers
    path('teachers/', views.teacher_list, name="teacher_list"),
    path('teachers/view/', views.teacher_view, name="teacher_view"),
    path('teachers/add/', views.teacher_add, name="teacher_add"),
    path('teachers/edit/', views.teacher_edit, name="teacher_edit"),

    # Departments
    path('departments/', views.department_list, name="department_list"),
    path('departments/add/', views.department_add, name="department_add"),

    # Subjects
    path('subjects/', views.subject_list, name="subject_list"),
    path('subjects/add/', views.subject_add, name="subject_add"),

    # Accounts
    path('accounts/fees-collection/', views.fees_collection, name="fees_collection"),
    path('accounts/expenses/', views.expenses, name="expenses"),
    path('accounts/salary/', views.salary, name="salary"),
    path('accounts/add-fees/', views.add_fees, name="add_fees"),
    path('accounts/add-expenses/', views.add_expenses, name="add_expenses"),
    path('accounts/add-salary/', views.add_salary, name="add_salary"),

    # Management
    path('holiday/', views.holiday, name="holiday"),
    path('fees/', views.fees, name="fees"),
    path('exam-list/', views.exam_list, name="exam_list"),
    path('events/', views.events, name="events"),
    path('timetable/', views.timetable, name="timetable"),
    path('library/', views.library, name="library"),

    # Authentication
    path('auth/login/', views.login, name="login"),
    path('auth/register/', views.register, name="register"),
    path('auth/forgot-password/', views.forgot_password, name="forgot_password"),

    # Pages
    path('blank-page/', views.blank_page, name="blank_page"),

    # Others
    path('sports/', views.sports, name="sports"),
]
