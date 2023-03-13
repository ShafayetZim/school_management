from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone


class Class(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Subject(models.Model):
    level = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Student(models.Model):
    student_code = models.CharField(max_length=250,blank=True, null= True)
    level = models.ForeignKey(Class, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=100, choices=[('Male','Male'),('Female','Female')], blank=True, null= True)
    dob = models.DateField(blank=True, null= True)
    contact = models.CharField(max_length=250, blank=True, null= True)

    def __str__(self):
        return self.student_code + " - " + self.first_name + " - " + self.last_name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    contact = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null = True)
    user_type = models.IntegerField(default = 2)
    gender = models.CharField(max_length=100, choices=[('Male','Male'),('Female','Female')], blank=True, null= True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Teacher.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(instance)
    try:
        profile = Teacher.objects.get(user = instance)
    except Exception as e:
        Teacher.objects.create(user=instance)
    instance.profile.save()


class ActiveClass(models.Model):
    assigned_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    assigned_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.CharField(max_length=250)

    def __str__(self):
        return self.assigned_class.name + '-' + self.assigned_subject.name + '-' + self.year


class ClassStudent(models.Model):
    classIns = models.ForeignKey(ActiveClass,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.CharField(max_length=250, null=True, blank=True)
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.student.student_code

    def get_grade_point(self):
        mark_int = int(self.mark) if self.mark else 0
        if mark_int >= 80:
            return 5.00
        elif mark_int >= 70:
            return 4.00
        elif mark_int >= 60:
            return 3.50
        elif mark_int >= 50:
            return 3.25
        elif mark_int >= 40:
            return 2.00
        elif mark_int >= 33:
            return 1.00
        else:
            return 0.00

    def get_letter_grade(self):
        mark_int = int(self.mark) if self.mark else 0
        if mark_int >= 80:
            return 'A+'
        elif mark_int >= 70:
            return 'A'
        elif mark_int >= 60:
            return 'A-'
        elif mark_int >= 50:
            return 'B'
        elif mark_int >= 40:
            return 'C'
        elif mark_int >= 33:
            return 'D'
        else:
            return 'F'

