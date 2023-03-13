from django.contrib import admin
from .models import Class, Subject, Student, Teacher, ActiveClass, ClassStudent

# Register your models here.

admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(ActiveClass)
admin.site.register(ClassStudent)
admin.site.register(Student)
