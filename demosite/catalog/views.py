from django.shortcuts import render
from .models import Dance_course, Instructor, Dance_course_instance, Style
from django.views import generic


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Dance_courses = Dance_course.objects.all().count()
    num_Dance_course_instances = Dance_course_instance.objects.all().count()

    # Currently ongoing courses (status = 'o')
    num_instances_ongoing = Dance_course_instance.objects.filter(running__exact='o').count()

    # The 'all()' is implied by default.
    num_instructors = Instructor.objects.count()

    # practice regex, icontains for case insensitive, contains for sensitive
    num_styles_with_letter = Style.objects.filter(name__icontains = 'o')

    # TODO courses with/ without partner

    context = {
        'num_Dance_courses': num_Dance_courses,
        'num_Dance_course_instances': num_Dance_course_instances,
        'num_instances_ongoing': num_instances_ongoing,
        'num_instructors': num_instructors,
        'num_styles_with_letter' : num_styles_with_letter
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# The generic view will query the database to get all records for the specified model
# Within the template you can access the list of books with the template
# variable named object_list OR dance_course_list (i.e. generically "<the model name>_list").
class Dance_courseListView(generic.ListView):
    model = Dance_course
    # renders a template expected to be located
    # at /demosite/catalog/templates/catalog/book_list.html
    # location can be overrun by doing the following:

    # your own name for the list as a template variable
    #context_object_name = 'xyz' # automaticallly would be 'dance_course_list'
    # do smth else if wanted, e.g specify specific objects that should be listed and not just everything
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # alternative to line above: already override the queryset function of ListView model
    # def get_queryset(self):
        #return Book.objects.filter(title__icontains='war')[:5]
    # override get_context_data() from super class to pass additional context variables to the template
    '''# def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context'''
    # Specify your own template name/location...doesnt work apparently?? back to basic folder location then
    #template_name = '/catalog/templates/dance_course_list.html'


class Dance_courseDetailView(generic.DetailView):
    model = Dance_course
    # Within the html template you can access the dance_course's
    # details with the template variable named object OR dance_course (i.e. generically "the_model_name").
    # canceld since didnt find this renaming:
    #template_name = '/catalog/templates/catalog/dance_course_detail.html'


# doing the detail view and such by hand and not using prebuilt, it would work like this, example:
'''def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'catalog/book_detail.html', context={'book': book})

'''
#  This is a shortcut to raise an Http404 exception if the record is not found.
'''
from django.shortcuts import get_object_or_404

def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'catalog/book_detail.html', context={'book': book})

'''
