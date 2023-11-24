from django.views.generic import ListView
from django.shortcuts import render

from .models import Student,Teacher,Students_tichers


def students_list(request):
    template = 'school/students_list.html'
    st=Student.objects.all()
    students=st.order_by('group')
    tt=Teacher.objects.all()
    st=Students_tichers.objects.all()
    context = {'object_list': students}


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

# def students_tichers_fill():
#
#     students_teachers=Students_tichers.objects.create(teacher=teacher,student=student)

