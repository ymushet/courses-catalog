from django.contrib import admin

from courses.models import Course


@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    ordering = ('start_at',)
