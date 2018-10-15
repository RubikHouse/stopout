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
    students = Student.objects.close_friends()
    context = {
        'school': school,
        'students': students,
    }
    return render(request, 'school/school_detail.html', context)


def student_list(request):
    students = Student.objects.all()

    context = {
        'students': students,
    }
    return render(request, 'school/student_list.html', context)


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    friends = Student.objects.close_friends
    context = {
        'student': student,
        'friends': friends,
    }
    return render(request, 'school/student_detail.html', context)
