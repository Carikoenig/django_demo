from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # the URL must already have matched /catalog (automatic redirection in demosite/demosite/urls.py), so the view will actually be called for the URL: /catalog/books/.
    # For Django class-based views we access an appropriate view function by calling the class method as_view().
    path('dance_courses/', views.Dance_courseListView.as_view(), name='dance_course_list'),
    # Warning: The generic class-based detail view expects to be passed a parameter named pk. If you're writing your own function view you can use whatever parameter name you like, or indeed pass the information in an unnamed argument.
    #  If you need more refined filtering (for example, to filter only strings that have a certain number of characters) then you can use the re_path() method.
    #This method is used just like path() except that it allows you to specify a pattern using a Regular expression: example: re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail')
    path('dance_course/<int:pk>', views.Dance_courseDetailView.as_view(), name='dance_course-detail'),
    path('instructors/', views.InstructorListView.as_view(), name='instructor_list'),
    path('instructor/<slug>', views.InstructorDetailView.as_view(), name='instructor-detail'),
    path('mycourses/', views.CoursesAttendedByUserListView.as_view(), name='my-courses'),
    path('attending_students/<uuid:pk>', views.Dance_course_ParticipantsDetailView.as_view(), name='attending-students'),

]
