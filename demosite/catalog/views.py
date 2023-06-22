from django.shortcuts import render

# Create your views here.

from .models import Dance_course, Instructor, Dance_course_instance, Style

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Dance_courses = Dance_course.objects.all().count()
    num_Dance_course_instances = Dance_course_instance.objects.all().count()

    # Currently ongoing courses (status = 'o')
    num_instances_ongoing = Dance_course_instance.objects.filter(running__exact='o').count()

    # The 'all()' is implied by default.
    num_instructors = Instructor.objects.count()

    context = {
        'num_Dance_courses': num_Dance_courses,
        'num_Dance_course_instances': num_Dance_course_instances,
        'num_instances_ongoing': num_instances_ongoing,
        'num_instructors': num_instructors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
