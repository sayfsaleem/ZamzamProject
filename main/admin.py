from django.contrib import admin
from .models import Courses, Teacher, Student,Event,Curriculum,Contact

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'language', 'price')
    list_filter = ('course_name', 'language')
    search_fields = ('course_name', 'language')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'nationality')
    list_filter = ('gender', 'nationality')
    search_fields = ('name', 'nationality')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'age', 'Teacher_language', 'start_time', 'end_time')
    list_filter = ('course', 'Teacher_language')
    search_fields = ('name', 'course__course_name', 'Teacher_language')
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','time','picture','location')
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('title','course','week_number','date','time')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'number', 'message')

admin.site.register(Contact, ContactAdmin)
