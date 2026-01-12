from django.shortcuts import render, redirect
from .models import Student, Subject, Attendance


def home(request):
    return render(request, 'attendance/home.html')


from django.shortcuts import render, redirect
from .models import Student, Subject, Attendance

def mark_attendance(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student")
        subject_id = request.POST.get("subject")
        status_value = request.POST.get("status")

        status = True if status_value == "present" else False

        Attendance.objects.create(
            student_id=student_id,
            subject_id=subject_id,
            status=status
        )

        return redirect('view_attendance')

    # 👇 THIS RETURN IS VERY IMPORTANT
    return render(request, 'attendance/mark_attendance.html', {
        'students': students,
        'subjects': subjects
    })




def view_attendance(request):
    records = Attendance.objects.all()
    return render(request, 'attendance/view_attendance.html', {
        'records': records
    })

from django.db.models import Count
from .models import Attendance

def dashboard(request):
    present_count = Attendance.objects.filter(status=True).count()
    absent_count = Attendance.objects.filter(status=False).count()

    return render(request, 'attendance/dashboard.html', {
        'present_count': present_count,
        'absent_count': absent_count
    })
