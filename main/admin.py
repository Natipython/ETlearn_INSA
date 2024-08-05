from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_desc']

admin.site.register(Course, CourseAdmin)


# Register models here.
