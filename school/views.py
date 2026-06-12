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

STUDENTS = [
    {"id": "PRE1234", "name": "Daisy Parks", "email": "daisy@gmail.com", "class_name": "X - A",
     "gender": "Female", "admission_date": "17 Nov 2020", "mobile": "+91 89657 48512",
     "status": "Active", "initials": "DP", "avatar_class": "avatar-purple"},
    {"id": "PRE1252", "name": "Joe Kelley", "email": "joe.kelley@gmail.com", "class_name": "IX - B",
     "gender": "Male", "admission_date": "17 Oct 2020", "mobile": "+91 89657 48522",
     "status": "Active", "initials": "JK", "avatar_class": "avatar-blue"},
    {"id": "PRE1434", "name": "Vincent Carpenter", "email": "vincent@gmail.com", "class_name": "VIII - A",
     "gender": "Male", "admission_date": "05 Nov 2020", "mobile": "+91 89657 48532",
     "status": "Active", "initials": "VC", "avatar_class": "avatar-orange"},
    {"id": "PRE1534", "name": "Lois Adams", "email": "lois.adams@gmail.com", "class_name": "X - C",
     "gender": "Female", "admission_date": "02 Oct 2020", "mobile": "+91 89657 48542",
     "status": "Inactive", "initials": "LA", "avatar_class": "avatar-pink"},
    {"id": "PRE2143", "name": "Levell Scott", "email": "levell.scott@gmail.com", "class_name": "VII - A",
     "gender": "Male", "admission_date": "04 Sept 2020", "mobile": "+91 89657 48552",
     "status": "Active", "initials": "LS", "avatar_class": "avatar-primary"},
    {"id": "PRE2153", "name": "Calvin Bautista", "email": "calvin.b@gmail.com", "class_name": "IX - A",
     "gender": "Male", "admission_date": "28 Oct 2020", "mobile": "+91 89657 48562",
     "status": "Active", "initials": "CB", "avatar_class": "avatar-purple"},
    {"id": "PRE2209", "name": "Ava Mitchell", "email": "ava.mitchell@gmail.com", "class_name": "VI - B",
     "gender": "Female", "admission_date": "17 Aug 2020", "mobile": "+91 89657 48572",
     "status": "Active", "initials": "AM", "avatar_class": "avatar-blue"},
    {"id": "PRE2213", "name": "Marcus Reed", "email": "marcus.reed@gmail.com", "class_name": "XI - A",
     "gender": "Male", "admission_date": "05 Aug 2020", "mobile": "+91 89657 48582",
     "status": "Inactive", "initials": "MR", "avatar_class": "avatar-orange"},
]


def student_list(request):
    return render(request, "students/list.html", {"students": STUDENTS})


def student_view(request):
    return render(request, "students/view.html")


def student_add(request):
    return render(request, "students/add.html")


def student_edit(request):
    student = {
        "first_name": "Daisy", "last_name": "Parks", "email": "daisy@gmail.com",
        "phone": "+91 89657 48512", "dob": "1995-04-22", "gender": "Female",
        "blood_group": "O+", "religion": "Christian", "category": "General",
        "class_name": "X", "section": "A", "admission_date": "2020-11-17",
        "current_address": "2118 Thornridge Cir. Syracuse, Connecticut 35624",
        "permanent_address": "2118 Thornridge Cir. Syracuse, Connecticut 35624",
        "city": "Syracuse", "state": "Connecticut", "postal_code": "35624", "country": "USA",
        "father_name": "Robert Parks", "mother_name": "Linda Parks",
        "guardian_relation": "Father", "guardian_phone": "+91 98765 43210",
        "guardian_email": "robert.parks@gmail.com", "guardian_occupation": "Engineer",
    }
    return render(request, "students/edit.html", {"student": student})


# ---------------------------------------------------------------------------
# Teachers
# ---------------------------------------------------------------------------

TEACHERS = [
    {"id": "PRE3001", "name": "Jonathan Kelley", "email": "jonathan@gmail.com", "department": "Computer Science",
     "subject": "Computer Science", "gender": "Male", "joining_date": "17 Nov 2020", "mobile": "+91 91234 56780",
     "status": "Active", "initials": "JK", "avatar_class": "avatar-blue"},
    {"id": "PRE3002", "name": "Sophia Turner", "email": "sophia.turner@gmail.com", "department": "Mathematics",
     "subject": "Mathematics", "gender": "Female", "joining_date": "12 Oct 2020", "mobile": "+91 91234 56781",
     "status": "Active", "initials": "ST", "avatar_class": "avatar-pink"},
    {"id": "PRE3003", "name": "Michael Brooks", "email": "michael.brooks@gmail.com", "department": "Science",
     "subject": "Physics", "gender": "Male", "joining_date": "05 Sept 2020", "mobile": "+91 91234 56782",
     "status": "Active", "initials": "MB", "avatar_class": "avatar-orange"},
    {"id": "PRE3004", "name": "Olivia Reyes", "email": "olivia.reyes@gmail.com", "department": "English",
     "subject": "English Literature", "gender": "Female", "joining_date": "21 Aug 2020", "mobile": "+91 91234 56783",
     "status": "Inactive", "initials": "OR", "avatar_class": "avatar-purple"},
    {"id": "PRE3005", "name": "Ethan Walker", "email": "ethan.walker@gmail.com", "department": "Science",
     "subject": "Chemistry", "gender": "Male", "joining_date": "30 Jul 2020", "mobile": "+91 91234 56784",
     "status": "Active", "initials": "EW", "avatar_class": "avatar-primary"},
    {"id": "PRE3006", "name": "Grace Coleman", "email": "grace.coleman@gmail.com", "department": "Arts",
     "subject": "Fine Arts", "gender": "Female", "joining_date": "14 Jul 2020", "mobile": "+91 91234 56785",
     "status": "Active", "initials": "GC", "avatar_class": "avatar-blue"},
]


def teacher_list(request):
    return render(request, "teachers/list.html", {"teachers": TEACHERS})


def teacher_view(request):
    return render(request, "teachers/view.html")


def teacher_add(request):
    return render(request, "teachers/add.html")


def teacher_edit(request):
    teacher = {
        "first_name": "Jonathan", "last_name": "Kelley", "email": "jonathan@gmail.com",
        "phone": "+91 91234 56780", "dob": "1990-01-12", "gender": "Male",
        "department": "Computer Science", "subject": "Computer Science", "designation": "Senior Teacher",
        "joining_date": "2020-11-17", "qualification": "M.Sc Computer Science", "experience": 8,
        "current_address": "2118 Thornridge Cir. Syracuse, Connecticut 35624",
        "permanent_address": "2118 Thornridge Cir. Syracuse, Connecticut 35624",
        "city": "Syracuse", "state": "Connecticut", "postal_code": "35624", "country": "USA",
        "basic_salary": 4500, "bank_name": "City Bank", "account_number": "0123456789",
    }
    return render(request, "teachers/edit.html", {"teacher": teacher})


# ---------------------------------------------------------------------------
# Departments & Subjects
# ---------------------------------------------------------------------------

DEPARTMENTS = [
    {"id": "DEP001", "name": "Computer Science", "head": "Jonathan Kelley", "total_staff": 12,
     "status": "Active", "initials": "JK", "avatar_class": "avatar-blue"},
    {"id": "DEP002", "name": "Mathematics", "head": "Sophia Turner", "total_staff": 9,
     "status": "Active", "initials": "ST", "avatar_class": "avatar-pink"},
    {"id": "DEP003", "name": "Science", "head": "Michael Brooks", "total_staff": 14,
     "status": "Active", "initials": "MB", "avatar_class": "avatar-orange"},
    {"id": "DEP004", "name": "English", "head": "Olivia Reyes", "total_staff": 7,
     "status": "Inactive", "initials": "OR", "avatar_class": "avatar-purple"},
    {"id": "DEP005", "name": "Arts", "head": "Grace Coleman", "total_staff": 5,
     "status": "Active", "initials": "GC", "avatar_class": "avatar-primary"},
]

SUBJECTS = [
    {"id": "SUB001", "name": "Computer Science", "code": "CS101", "type": "Theory", "department": "Computer Science"},
    {"id": "SUB002", "name": "Data Structures", "code": "CS102", "type": "Practical", "department": "Computer Science"},
    {"id": "SUB003", "name": "Algebra", "code": "MA101", "type": "Theory", "department": "Mathematics"},
    {"id": "SUB004", "name": "Physics", "code": "SC101", "type": "Theory", "department": "Science"},
    {"id": "SUB005", "name": "Chemistry Lab", "code": "SC102", "type": "Practical", "department": "Science"},
    {"id": "SUB006", "name": "English Literature", "code": "EN101", "type": "Theory", "department": "English"},
]


def department_list(request):
    return render(request, "departments/list.html", {"departments": DEPARTMENTS})


def department_add(request):
    return render(request, "departments/add.html")


def subject_list(request):
    return render(request, "subjects/list.html", {"subjects": SUBJECTS})


def subject_add(request):
    return render(request, "subjects/add.html")


# ---------------------------------------------------------------------------
# Accounts
# ---------------------------------------------------------------------------

FEES = [
    {"id": "PRE1234", "student_name": "Daisy Parks", "class_name": "X - A", "fees_type": "Tuition Fees",
     "amount": "$500", "payment_date": "17 Nov 2020", "status": "Paid", "initials": "DP", "avatar_class": "avatar-purple"},
    {"id": "PRE1252", "student_name": "Joe Kelley", "class_name": "IX - B", "fees_type": "Transport Fees",
     "amount": "$120", "payment_date": "17 Oct 2020", "status": "Paid", "initials": "JK", "avatar_class": "avatar-blue"},
    {"id": "PRE1434", "student_name": "Vincent Carpenter", "class_name": "VIII - A", "fees_type": "Library Fees",
     "amount": "$50", "payment_date": "05 Nov 2020", "status": "Unpaid", "initials": "VC", "avatar_class": "avatar-orange"},
    {"id": "PRE1534", "student_name": "Lois Adams", "class_name": "X - C", "fees_type": "Exam Fees",
     "amount": "$80", "payment_date": "02 Oct 2020", "status": "Pending", "initials": "LA", "avatar_class": "avatar-pink"},
    {"id": "PRE2143", "student_name": "Levell Scott", "class_name": "VII - A", "fees_type": "Tuition Fees",
     "amount": "$500", "payment_date": "04 Sept 2020", "status": "Paid", "initials": "LS", "avatar_class": "avatar-primary"},
    {"id": "PRE2153", "student_name": "Calvin Bautista", "class_name": "IX - A", "fees_type": "Hostel Fees",
     "amount": "$300", "payment_date": "28 Oct 2020", "status": "Unpaid", "initials": "CB", "avatar_class": "avatar-purple"},
]

EXPENSES = [
    {"id": "PRE1252", "item_name": "Water Bottle", "item_quantity": 267, "amount": "$237",
     "purchase_source": "DJ Stationary", "purchase_date": "17 Oct 2020"},
    {"id": "PRE1534", "item_name": "Hard disk", "item_quantity": 2, "amount": "$560",
     "purchase_source": "Sony Center", "purchase_date": "02 Oct 2020"},
    {"id": "PRE1536", "item_name": "Hard disk", "item_quantity": 3, "amount": "$560",
     "purchase_source": "Music Center", "purchase_date": "02 Oct 2020"},
    {"id": "PRE2143", "item_name": "Desk", "item_quantity": 6, "amount": "$378",
     "purchase_source": "Take Away", "purchase_date": "04 Sept 2020"},
    {"id": "PRE2153", "item_name": "Note books", "item_quantity": 100, "amount": "$236",
     "purchase_source": "DJ Stationary", "purchase_date": "28 Oct 2020"},
    {"id": "PRE2209", "item_name": "Chair", "item_quantity": 6, "amount": "$120",
     "purchase_source": "Abc Shop", "purchase_date": "17 Aug 2020"},
    {"id": "PRE2213", "item_name": "Table", "item_quantity": 2, "amount": "$56",
     "purchase_source": "Online", "purchase_date": "05 Aug 2020"},
    {"id": "PRE2431", "item_name": "Projector", "item_quantity": 1, "amount": "$246",
     "purchase_source": "Real Shop", "purchase_date": "17 Sept 2020"},
]

SALARIES = [
    {"id": "PRE1234", "name": "Nathan Humphries", "designation": "Senior Teacher", "gender": "Male",
     "joining_date": "17 Nov 2020", "amount": "$4,500", "status": "Paid", "initials": "NH", "avatar_class": "avatar-orange"},
    {"id": "PRE1252", "name": "Joe Kelley", "designation": "Teacher", "gender": "Female",
     "joining_date": "17 Oct 2020", "amount": "$3,800", "status": "Paid", "initials": "JK", "avatar_class": "avatar-pink"},
    {"id": "PRE1434", "name": "Vincent Carpenter", "designation": "Lab Assistant", "gender": "Male",
     "joining_date": "05 Nov 2020", "amount": "$2,200", "status": "Pending", "initials": "VC", "avatar_class": "avatar-blue"},
    {"id": "PRE1534", "name": "Lois Adams", "designation": "Librarian", "gender": "Male",
     "joining_date": "02 Oct 2020", "amount": "$2,500", "status": "Paid", "initials": "LA", "avatar_class": "avatar-purple"},
    {"id": "PRE2143", "name": "Levell Scott", "designation": "Teacher", "gender": "Male",
     "joining_date": "04 Sept 2020", "amount": "$3,600", "status": "Paid", "initials": "LS", "avatar_class": "avatar-primary"},
    {"id": "PRE2153", "name": "Calvin Bautista", "designation": "Accountant", "gender": "Male",
     "joining_date": "28 Oct 2020", "amount": "$3,000", "status": "Pending", "initials": "CB", "avatar_class": "avatar-orange"},
]


def fees_collection(request):
    return render(request, "accounts/fees_collection.html", {"fees": FEES})


def expenses(request):
    return render(request, "accounts/expenses.html", {"expenses": EXPENSES})


def salary(request):
    return render(request, "accounts/salary.html", {"salaries": SALARIES})


def add_fees(request):
    return render(request, "accounts/add_fees.html")


def add_expenses(request):
    return render(request, "accounts/add_expenses.html")


def add_salary(request):
    return render(request, "accounts/add_salary.html")


# ---------------------------------------------------------------------------
# Holiday, Fees structure, Exam list, Events, Time Table, Library
# ---------------------------------------------------------------------------

HOLIDAYS = [
    {"id": 1, "name": "New Year's Day", "date": "01 Jan 2025", "day": "Wednesday", "description": "New year holiday for all staff and students"},
    {"id": 2, "name": "Republic Day", "date": "26 Jan 2025", "day": "Monday", "description": "National holiday"},
    {"id": 3, "name": "Spring Break", "date": "10 Mar 2025", "day": "Monday", "description": "One week spring break"},
    {"id": 4, "name": "Independence Day", "date": "15 Aug 2025", "day": "Friday", "description": "National holiday"},
    {"id": 5, "name": "Teachers' Day", "date": "05 Sept 2025", "day": "Friday", "description": "Celebration for all teaching staff"},
    {"id": 6, "name": "Autumn Break", "date": "20 Oct 2025", "day": "Monday", "description": "One week autumn break"},
    {"id": 7, "name": "Christmas Day", "date": "25 Dec 2025", "day": "Thursday", "description": "Christmas holiday"},
    {"id": 8, "name": "Winter Break", "date": "29 Dec 2025", "day": "Monday", "description": "Winter vacation for all students"},
]

FEES_STRUCTURE = [
    {"id": 1, "class_name": "Class I - V", "fees_type": "Tuition Fees", "amount": "$300", "due_date": "10 Jan 2025", "status": "Active"},
    {"id": 2, "class_name": "Class VI - VIII", "fees_type": "Tuition Fees", "amount": "$400", "due_date": "10 Jan 2025", "status": "Active"},
    {"id": 3, "class_name": "Class IX - X", "fees_type": "Tuition Fees", "amount": "$500", "due_date": "10 Jan 2025", "status": "Active"},
    {"id": 4, "class_name": "Class XI - XII", "fees_type": "Tuition Fees", "amount": "$600", "due_date": "10 Jan 2025", "status": "Active"},
    {"id": 5, "class_name": "All Classes", "fees_type": "Transport Fees", "amount": "$120", "due_date": "15 Jan 2025", "status": "Active"},
    {"id": 6, "class_name": "All Classes", "fees_type": "Library Fees", "amount": "$50", "due_date": "15 Jan 2025", "status": "Inactive"},
    {"id": 7, "class_name": "All Classes", "fees_type": "Exam Fees", "amount": "$80", "due_date": "01 Mar 2025", "status": "Active"},
    {"id": 8, "class_name": "Hostel Students", "fees_type": "Hostel Fees", "amount": "$300", "due_date": "10 Jan 2025", "status": "Active"},
]

EXAMS = [
    {"id": 1, "name": "Mid Term Examination", "class_name": "X - A", "subject": "Mathematics", "date": "12 Dec 2025", "time": "09:00 AM - 11:00 AM", "status": "Pending"},
    {"id": 2, "name": "Mid Term Examination", "class_name": "X - A", "subject": "Science", "date": "13 Dec 2025", "time": "09:00 AM - 11:00 AM", "status": "Pending"},
    {"id": 3, "name": "Mid Term Examination", "class_name": "X - A", "subject": "English", "date": "14 Dec 2025", "time": "09:00 AM - 11:00 AM", "status": "Pending"},
    {"id": 4, "name": "Unit Test 2", "class_name": "IX - B", "subject": "Computer Science", "date": "20 Nov 2025", "time": "10:00 AM - 11:00 AM", "status": "Completed"},
    {"id": 5, "name": "Unit Test 2", "class_name": "IX - B", "subject": "Mathematics", "date": "21 Nov 2025", "time": "10:00 AM - 11:00 AM", "status": "Completed"},
    {"id": 6, "name": "Final Examination", "class_name": "XII - A", "subject": "Physics", "date": "05 Jan 2026", "time": "09:00 AM - 12:00 PM", "status": "Pending"},
    {"id": 7, "name": "Final Examination", "class_name": "XII - A", "subject": "Chemistry", "date": "07 Jan 2026", "time": "09:00 AM - 12:00 PM", "status": "Pending"},
]

EVENTS = [
    {"day": "15", "month": "Aug", "title": "Independence Day Celebration", "time": "08:00 AM - 10:00 AM",
     "venue": "School Ground", "description": "Flag hoisting ceremony followed by cultural programs.", "status": "Active"},
    {"day": "05", "month": "Sep", "title": "Teachers' Day Program", "time": "09:00 AM - 12:00 PM",
     "venue": "Main Auditorium", "description": "Special assembly and performances by students for teachers.", "status": "Active"},
    {"day": "20", "month": "Oct", "title": "Annual Sports Meet", "time": "08:00 AM - 04:00 PM",
     "venue": "Sports Complex", "description": "Inter-house athletic competitions and award ceremony.", "status": "Active"},
    {"day": "12", "month": "Nov", "title": "Science Exhibition", "time": "10:00 AM - 03:00 PM",
     "venue": "Science Block", "description": "Students showcase science projects and experiments.", "status": "Active"},
    {"day": "25", "month": "Dec", "title": "Christmas Celebration", "time": "11:00 AM - 01:00 PM",
     "venue": "Main Auditorium", "description": "Carol singing, gift exchange and festive activities.", "status": "Inactive"},
    {"day": "26", "month": "Jan", "title": "Republic Day Parade", "time": "08:00 AM - 09:30 AM",
     "venue": "School Ground", "description": "Flag hoisting and march-past by student contingents.", "status": "Active"},
]

PERIODS = ["Period 1\n9:00 - 9:45", "Period 2\n9:45 - 10:30", "Period 3\n10:45 - 11:30",
           "Period 4\n11:30 - 12:15", "Lunch", "Period 5\n1:00 - 1:45", "Period 6\n1:45 - 2:30"]

TIMETABLE = [
    {"day": "Monday", "periods": [
        {"subject": "Mathematics", "teacher": "S. Turner"}, {"subject": "Physics", "teacher": "M. Brooks"},
        {"subject": "English", "teacher": "O. Reyes"}, {"subject": "Computer Science", "teacher": "J. Kelley"},
        {"subject": "Break", "teacher": ""}, {"subject": "Chemistry", "teacher": "E. Walker"},
        {"subject": "Fine Arts", "teacher": "G. Coleman"},
    ]},
    {"day": "Tuesday", "periods": [
        {"subject": "Physics", "teacher": "M. Brooks"}, {"subject": "Mathematics", "teacher": "S. Turner"},
        {"subject": "Computer Science", "teacher": "J. Kelley"}, {"subject": "English", "teacher": "O. Reyes"},
        {"subject": "Break", "teacher": ""}, {"subject": "Fine Arts", "teacher": "G. Coleman"},
        {"subject": "Chemistry", "teacher": "E. Walker"},
    ]},
    {"day": "Wednesday", "periods": [
        {"subject": "English", "teacher": "O. Reyes"}, {"subject": "Chemistry", "teacher": "E. Walker"},
        {"subject": "Mathematics", "teacher": "S. Turner"}, {"subject": "Physics", "teacher": "M. Brooks"},
        {"subject": "Break", "teacher": ""}, {"subject": "Computer Science", "teacher": "J. Kelley"},
        {"subject": "Fine Arts", "teacher": "G. Coleman"},
    ]},
    {"day": "Thursday", "periods": [
        {"subject": "Computer Science", "teacher": "J. Kelley"}, {"subject": "Fine Arts", "teacher": "G. Coleman"},
        {"subject": "Physics", "teacher": "M. Brooks"}, {"subject": "Mathematics", "teacher": "S. Turner"},
        {"subject": "Break", "teacher": ""}, {"subject": "English", "teacher": "O. Reyes"},
        {"subject": "Chemistry", "teacher": "E. Walker"},
    ]},
    {"day": "Friday", "periods": [
        {"subject": "Chemistry", "teacher": "E. Walker"}, {"subject": "Computer Science", "teacher": "J. Kelley"},
        {"subject": "Fine Arts", "teacher": "G. Coleman"}, {"subject": "English", "teacher": "O. Reyes"},
        {"subject": "Break", "teacher": ""}, {"subject": "Mathematics", "teacher": "S. Turner"},
        {"subject": "Physics", "teacher": "M. Brooks"},
    ]},
    {"day": "Saturday", "periods": [
        {"subject": "Fine Arts", "teacher": "G. Coleman"}, {"subject": "English", "teacher": "O. Reyes"},
        {"subject": "Chemistry", "teacher": "E. Walker"}, {"subject": "Computer Science", "teacher": "J. Kelley"},
        {"subject": "Break", "teacher": ""}, {"subject": "Physics", "teacher": "M. Brooks"},
        {"subject": "Mathematics", "teacher": "S. Turner"},
    ]},
]

BOOKS = [
    {"id": "LIB001", "title": "Introduction to Algorithms", "author": "T. Cormen", "subject": "Computer Science", "quantity": 12, "available": 5, "status": "Available"},
    {"id": "LIB002", "title": "A Brief History of Time", "author": "S. Hawking", "subject": "Physics", "quantity": 8, "available": 0, "status": "Issued"},
    {"id": "LIB003", "title": "Calculus Made Easy", "author": "S. Thompson", "subject": "Mathematics", "quantity": 15, "available": 9, "status": "Available"},
    {"id": "LIB004", "title": "To Kill a Mockingbird", "author": "H. Lee", "subject": "English", "quantity": 10, "available": 4, "status": "Available"},
    {"id": "LIB005", "title": "Organic Chemistry", "author": "J. Clayden", "subject": "Chemistry", "quantity": 6, "available": 0, "status": "Issued"},
    {"id": "LIB006", "title": "The Art of Computer Programming", "author": "D. Knuth", "subject": "Computer Science", "quantity": 4, "available": 2, "status": "Available"},
]


def holiday(request):
    return render(request, "holiday/list.html", {"holidays": HOLIDAYS})


def fees(request):
    return render(request, "fees/list.html", {"fees_structure": FEES_STRUCTURE})


def exam_list(request):
    return render(request, "exam/list.html", {"exams": EXAMS})


def events(request):
    return render(request, "events/list.html", {"events": EVENTS})


def timetable(request):
    return render(request, "timetable/list.html", {"periods": PERIODS, "timetable": TIMETABLE})


def library(request):
    return render(request, "library/list.html", {"books": BOOKS})


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


SPORTS = [
    {"name": "Football", "coach": "David Miller", "members": 22, "icon": "bi-dribbble", "bg_class": "bg-blue"},
    {"name": "Basketball", "coach": "James Carter", "members": 15, "icon": "bi-circle", "bg_class": "bg-orange"},
    {"name": "Cricket", "coach": "Robert Hughes", "members": 16, "icon": "bi-bullseye", "bg_class": "bg-purple"},
    {"name": "Athletics", "coach": "Emma Wilson", "members": 30, "icon": "bi-lightning-fill", "bg_class": "bg-pink"},
]


def sports(request):
    return render(request, "sports/list.html", {"sports": SPORTS})
