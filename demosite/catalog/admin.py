from django.contrib import admin
from .models import Style, Language, Dance_course, Dance_course_instance, Instructor

# Register the models here
admin.site.register(Style)
admin.site.register(Language)
admin.site.register(Dance_course)
admin.site.register(Dance_course_instance)
admin.site.register(Instructor)
