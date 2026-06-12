from django.contrib import admin
from .models import Student, Parent

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    list_filter = ('father_name', 'mother_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'student_class', 'section', 'gender','joining_date', 'addmission_number', 'mobile_number')
    search_fields = ('first_name', 'last_name', 'student_id', 'student_class', 'addmission_number')
    list_filter = ('gender', 'student_class', 'section')
    readonly_fields = ('student_image',)




    