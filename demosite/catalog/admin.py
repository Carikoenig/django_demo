from django.contrib import admin
from .models import Style, Language, Dance_course, Dance_course_instance, Instructor

# Register the models here
admin.site.register(Style)
admin.site.register(Language)
# admin.site.register(Dance_course)
# admin.site.register(Dance_course_instance)
# admin.site.register(Instructor)


class Dance_course_instanceInline(admin.TabularInline):
    model = Dance_course_instance
    # by setting the extra attribute to 0,no placeholder not existing instances are shown in the lower part of the inline
    extra = 0


# Define the admin class
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'display_language')

    fields = [('first_name', 'last_name'), ('date_of_birth', 'speaks_language'), 'slug']

    prepopulated_fields = {"slug": ("first_name", "last_name",)}


# Register the admin class with the associated model
admin.site.register(Instructor, InstructorAdmin)


# Register the Admin classes for Dance_course using the decorator
@admin.register(Dance_course)
class Dance_courseAdmin(admin.ModelAdmin):
    list_display = ('title', 'style')

    inlines = [Dance_course_instanceInline]

# Register the Admin classes for Dance_course_Instance using the decorator
@admin.register(Dance_course_instance)
class Dance_course_instanceAdmin(admin.ModelAdmin):
    list_display = ('display_dancecourse', 'display_instructor', 'running', 'start_date')
    list_filter = ('running', 'instructor')
    fieldsets = (
        (None, {
            'fields': ('dance_course', 'instructor')
        }),
        ('Runtime', {
            'fields': ('start_date', 'running')
        }),
    )
