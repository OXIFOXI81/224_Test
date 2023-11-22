from django.contrib import admin

from .models import Student, Teacher,Students_tichers

class Students_tichersInline(admin.TabularInline):
      model=Students_tichers
      extra=3


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
   # list_display = ['name','group']
   # list_filter = ['name']
   list_display = ['id']
   # inlines = [Students_tichersInline,]
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    inlines = [Students_tichersInline, ]


