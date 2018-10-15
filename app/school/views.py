# fbc(function-based view)

from django.shortcuts import render

from .models import *


def school_list(request):
    schools = School.objects.all()

    context = {
        'schools': schools,
    }
    return render(request, 'school/school_list.html', context)


def school_detail(request, pk):
    school = School.objects.get(id=pk)
    context = {
        'school': school,
    }
    return render(request, 'school/school_detail.html', context)


def student_list(request):
    students = Student.objects.all()

    context = {
        'students': students,
    }
    return render(request, 'school/student_list.html', context)


def student_detail(request, pk):
    student = School.objects.get(id=pk)
    context = {
        'student': student,
    }
    return render(request, 'school/student_detail.html', context)
