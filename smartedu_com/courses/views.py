from django.shortcuts import render
from . models import Course, Category, Tag
from django.shortcuts import get_object_or_404

def course_list(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()
    current_user = request.user

    if category_slug != None:
        if current_user.is_authenticated:
            enrolled_course = current_user.courses_joined.all()
            category_page = get_object_or_404(Category, slug=category_slug)
            courses = Course.objects.filter(available=True, category= category_page)
            for course in enrolled_course:
                courses = courses.exclude(id = course.id)
        else:
            category_page = get_object_or_404(Category, slug=category_slug)
            courses = Course.objects.filter(available=True, category= category_page)

    elif tag_slug != None:
        if current_user.is_authenticated:
            enrolled_course = current_user.courses_joined.all()
            tag_page = get_object_or_404(Tag, slug=tag_slug)
            courses = Course.objects.filter(available=True, tags=tag_page)
            for course in enrolled_course:
                courses = courses.exclude(id = course.id)
        else:
            tag_page = get_object_or_404(Tag, slug=tag_slug)
            courses = Course.objects.filter(available=True, tags=tag_page)

    else:
        #courses = Course.objects.all().order_by('-date')
        if current_user.is_authenticated:
            enrolled_course = current_user.courses_joined.all()
            courses = Course.objects.all().order_by('-date')
            for course in enrolled_course:
                courses = courses.exclude(id = course.id)
        else:
            courses = Course.objects.all().order_by('-date')

    context = {
        'courses':courses,
        'categories':categories,
        'tags':tags
    }

    return render(request, 'courses.html', context)   
    

def course_detail(request, category_slug, course_id):
    current_user = request.user
    courses = Course.objects.all().order_by('-date')
    course = Course.objects.get(category__slug = category_slug,id = course_id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()
    else:
        enrolled_courses = courses

    context = {
        'course':course,
        'enrolled_courses':enrolled_courses,
        'categories':categories,
        'tags':tags
    }

    return render(request, 'course.html', context)

def search(request):
    courses = Course.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses':courses,
        'categories':categories,
        'tags':tags
    }

    return render(request, 'courses.html', context)


"""def course_list(request):
    courses = Course.objects.order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses':courses,
        'categories':categories,
        'tags':tags
    }

    return render(request, 'courses.html', context)"""

"""def category_list(request, category_slug):
    courses = Course.objects.all().filter(category__slug = category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses':courses,
        'categories':categories,
        'tags':tags
    }

    return render(request, 'courses.html', context)"""

"""def tag_list(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug = tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses':courses,
        'categories':categories,
        'tags':tags
    }

    return render(request, 'courses.html', context)"""

