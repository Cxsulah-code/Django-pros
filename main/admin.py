from django.contrib import admin
from main.models import Teacher, Course, Student
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin): 
  
  list_display = ["id", "first_name", "last_name", "gender"]
  
  search_field = ["first_name", "last_name"]
  
  list_filter = ["first_name", "gender"]
  
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title"]
    
    search_field = ["title"]
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ["id", "first_name", "last_name", "gender"]