from django.shortcuts import render
from . models import Course

def course_list(request):
    courses = Course.objects.order_by('-date')

    context = {
        'courses':courses
    }

    return render(request, 'courses.html', context)

