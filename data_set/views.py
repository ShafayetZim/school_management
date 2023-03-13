from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Count, Q, F, FloatField, Sum
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from school_management.settings import MEDIA_ROOT, MEDIA_URL
from data_set.models import ActiveClass, Subject, Student, Class, ClassStudent, Teacher

from data_set.forms import SaveActiveClass, SaveSubject, SaveClass, SaveStudent, SaveClassStudent, UpdateTeacher, UserRegistration, UpdateProfileMeta


deparment_list = Class.objects.all()
context = {
    'page_title' : 'Simple Blog Site',
    'deparment_list' : deparment_list,
    'deparment_list_limited' : deparment_list[:3]
}

def home(request):
    context['page_title'] = 'Home'

    # context['posts'] = posts
    return render(request, 'home.html',context)

@login_required
def class_list(request):
    level = Class.objects.all()
    context['page_title'] = "Class List"
    context['level'] = level
    return render(request, 'class/class_list.html', context)

@login_required
def manage_class(request, pk=None):
    if pk == None:
        level = {}
    elif pk > 0:
        level = Class.objects.filter(id=pk).first()
    else:
        level = {}
    context['page_title'] = "Manage Class"
    context['level'] = level

    return render(request, 'class/manage_class.html', context)


def save_class(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        level = None
        print(not request.POST['id'] == '')
        if not request.POST['id'] == '':
            level = Class.objects.filter(id=request.POST['id']).first()
        if not level == None:
            form = SaveClass(request.POST, instance=level)
        else:
            form = SaveClass(request.POST)
    if form.is_valid():
        form.save()
        resp['status'] = 'success'
        messages.success(request, 'Class has been saved successfully')
    else:
        for field in form:
            for error in field.errors:
                resp['msg'] += str(error + '<br>')
        if not level == None:
            form = SaveClass(instance=level)

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_class(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        id = request.POST['id']
        try:
            level = Class.objects.filter(id=id).first()
            level.delete()
            resp['status'] = 'success'
            messages.success(request, 'Class has been deleted successfully.')
        except Exception as e:
            raise print(e)
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def subject(request):
    subjects = Subject.objects.all()
    context['page_title'] = "Subject Management"
    context['subjects'] = subjects
    return render(request, 'subject/subject_list.html', context)

@login_required
def manage_subject(request, pk=None):
    if pk == None:
        subject = {}
        level = Class.objects.all()
    elif pk > 0:
        subject = Subject.objects.filter(id=pk).first()
        level = Class.objects.all()
    else:
        subject = {}
        level = Class.objects.all()
    context['page_title'] = "Manage Subject"
    context['level'] = level
    context['subject'] = subject

    return render(request, 'subject/manage_subject.html', context)


def save_subject(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        subject = None
        print(not request.POST['id'] == '')
        if not request.POST['id'] == '':
            subject = Subject.objects.filter(id=request.POST['id']).first()
        if not subject == None:
            form = SaveSubject(request.POST, instance=subject)
        else:
            form = SaveSubject(request.POST)
    if form.is_valid():
        form.save()
        resp['status'] = 'success'
        messages.success(request, 'Subject has been saved successfully')
    else:
        for field in form:
            for error in field.errors:
                resp['msg'] += str(error + '<br>')
        if not subject == None:
            form = SaveSubject(instance=subject)

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_subject(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        id = request.POST['id']
        try:
            subject = Subject.objects.filter(id=id).first()
            subject.delete()
            resp['status'] = 'success'
            messages.success(request, 'Subject has been deleted successfully.')
        except Exception as e:
            raise print(e)
    return HttpResponse(json.dumps(resp), content_type="application/json")


#student
@login_required
def student(request):
    students = Student.objects.all()
    context['page_title'] = "Student List"
    context['students'] = students
    return render(request, 'student/student_list.html', context)

@login_required
def manage_student(request, pk=None):
    # course = course.objects.all()
    if pk == None:
        student = {}
        level = Class.objects.all()
    elif pk > 0:
        student = Student.objects.filter(id=pk).first()
        level = Class.objects.all()
    else:
        level = Class.objects.all()
        student = {}
    context['page_title'] = "Manage Student"
    context['level'] = level
    context['student'] = student

    return render(request, 'student/manage_student.html', context)

@login_required
def view_student(request, pk=None):
    if pk == None:
        student = {}
    elif pk > 0:
        student = Student.objects.filter(id=pk).first()
    else:
        student = {}
    context['student'] = student
    return render(request, 'student/student_details.html', context)


def save_student(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        student = None
        print(not request.POST['id'] == '')
        if not request.POST['id'] == '':
            student = Student.objects.filter(id=request.POST['id']).first()
        if not student == None:
            form = SaveStudent(request.POST, instance=student)
        else:
            form = SaveStudent(request.POST)
    if form.is_valid():
        form.save()
        resp['status'] = 'success'
        messages.success(request, 'Student Details has been saved successfully')
    else:
        for field in form:
            for error in field.errors:
                resp['msg'] += str(error + '<br>')
        if not student == None:
            form = SaveStudent(instance=subject)

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_student(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        id = request.POST['id']
        try:
            student = Student.objects.filter(id=id).first()
            student.delete()
            resp['status'] = 'success'
            messages.success(request, 'Student Details has been deleted successfully.')
        except Exception as e:
            raise print(e)
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def teacher(request):
    user = Teacher.objects.filter(user_type=2).all()
    context['page_title'] = "Teacher List"
    context['teachers'] = user
    return render(request, 'teacher/teacher_list.html', context)

@login_required
def manage_teacher(request, pk=None):
    if pk == None:
        teacher = {}
    elif pk > 0:
        teacher = Teacher.objects.filter(id=pk).first()
    else:
        teacher = {}
    context['page_title'] = "Manage Teacher"
    context['teacher'] = teacher
    return render(request, 'teacher/manage_teacher.html', context)

@login_required
def view_teacher(request, pk=None):
    if pk == None:
        teacher = {}
    elif pk > 0:
        teacher = Teacher.objects.filter(id=pk).first()
    else:
        teacher = {}
    context['page_title'] = "Manage Teacher"
    context['teacher'] = teacher
    return render(request, 'teacher/teacher_details.html', context)


def save_teacher(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        data = request.POST
        if data['id'].isnumeric() and data['id'] != '':
            user = User.objects.get(id=data['id'])
        else:
            user = None
        if not user == None:
            form = UpdateTeacher(data=data, user=user, instance=user)
        else:
            form = UserRegistration(data)
        if form.is_valid():
            form.save()

            if user == None:
                user = User.objects.all().last()
            try:
                profile = Teacher.objects.get(user=user)
            except:
                profile = None
            if profile is None:
                form2 = UpdateProfileMeta(request.POST, request.FILES)
            else:
                form2 = UpdateProfileMeta(request.POST, request.FILES, instance=profile)
                if form2.is_valid():
                    form2.save()
                    resp['status'] = 'success'
                    messages.success(request, 'Teacher has been save successfully.')
                else:
                    User.objects.filter(id=user.id).delete()
                    for field in form2:
                        for error in field.errors:
                            resp['msg'] += str(error + '<br>')

        else:
            for field in form:
                for error in field.errors:
                    resp['msg'] += str(error + '<br>')

    return HttpResponse(json.dumps(resp), content_type='application/json')


@login_required
def delete_teacher(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        id = request.POST['id']
        try:
            teacher = User.objects.filter(id=id).first()
            teacher.delete()
            resp['status'] = 'success'
            messages.success(request, 'Teacher has been deleted successfully.')
        except Exception as e:
            raise print(e)
    return HttpResponse(json.dumps(resp), content_type="application/json")


# Active Class
@login_required
def active_class(request):
    context = {}
    if request.user.is_authenticated:
        if request.user.profile.user_type == 2:  # Teacher user
            classes = ActiveClass.objects.filter(assigned_teacher=request.user.profile).all()
        else:
            classes = ActiveClass.objects.all()
        context['page_title'] = "Class Management"
        context['classes'] = classes
        return render(request, 'assigned/active_class_list.html', context)
    else:
        return redirect('login')


@login_required
def manage_active_class(request, pk=None):
    teacher = Teacher.objects.filter(user_type=2).all()
    level = Class.objects.all()
    subject = Subject.objects.all()
    if pk == None:
        _class = {}
    elif pk > 0:
        _class = ActiveClass.objects.filter(id=pk).first()
    else:
        _class = {}
    context['page_title'] = "Manage Active Class"
    context['teacher'] = teacher
    context['level'] = level
    context['subject'] = subject
    context['class'] = _class

    return render(request, 'assigned/manage_active_class.html', context)

@login_required
def view_active_class(request, pk=None):
    if pk is None:
        return redirect('home-page')
    else:
        _class = ActiveClass.objects.filter(id=pk).first()
        students = ClassStudent.objects.filter(classIns=_class).all()
        context['class'] = _class
        context['students'] = students
        context['page_title'] = "Class Information"
    return render(request, 'result/active_class_details.html', context)


def save_active_class(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        _class = None
        print(not request.POST['id'] == '')
        if not request.POST['id'] == '':
            _class = ActiveClass.objects.filter(id=request.POST['id']).first()
        if not _class == None:
            form = SaveActiveClass(request.POST, instance=_class)
        else:
            form = SaveActiveClass(request.POST)
    if form.is_valid():
        form.save()
        resp['status'] = 'success'
        messages.success(request, 'Class has been assigned successfully')
    else:
        for field in form:
            for error in field.errors:
                resp['msg'] += str(error + '<br>')
        if not _class == None:
            form = SaveActiveClass(instance=_class)

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_active_class(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        id = request.POST['id']
        try:
            _class = ActiveClass.objects.filter(id=id).first()
            _class.delete()
            resp['status'] = 'success'
            messages.success(request, 'Assigned Class has been deleted successfully.')
        except Exception as e:
            raise print(e)
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_assigned_student(request, pk=None):
    active_class = get_object_or_404(ActiveClass, pk=pk)
    students = Student.objects.filter(level=active_class.assigned_class)

    context = {
        'active_class': active_class,
        'students': students,
    }
    return render(request, 'assigned/assigned_student.html', context)

@login_required
def active_class_result(request):
    if request.user.is_authenticated:
        if request.user.profile.user_type == 2:  # Teacher user
            classes = ActiveClass.objects.filter(assigned_teacher=request.user.profile).all()
        else:
            classes = ActiveClass.objects.all()

    context['page_title'] = "Class Management"
    context['classes'] = classes
    return render(request, 'result/result_list.html', context)

@login_required
def manage_class_student(request, classPK=None):
    context = {}
    if classPK is None:
        return HttpResponse('Class ID is Unknown')
    else:
        context['classPK'] = classPK
        _class = ActiveClass.objects.get(id=classPK)
        students = Student.objects.filter(level=_class.assigned_class).exclude(
            id__in=ClassStudent.objects.filter(classIns=_class).values('student')
        ).all()
        context['students'] = students
        context['class'] = _class
        return render(request, 'result/manage_class_student.html', context)



def save_class_student(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        form = SaveClassStudent(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student has been added successfully.")
            resp['status'] = 'success'
        else:
            for field in form:
                for error in field.errors:
                    resp['msg'] += str(error + "<br>")
    return HttpResponse(json.dumps(resp), content_type='json')

@login_required
def delete_class_student(request):
    resp = {'status': 'failed', 'msg': ''}
    if request.method == 'POST':
        id = request.POST['id']
        try:
            cs = ClassStudent.objects.filter(id=id).first()
            cs.delete()
            resp['status'] = 'success'
            messages.success(request, 'Students mark has been deleted from Class successfully.')
        except Exception as e:
            raise print(e)
    return HttpResponse(json.dumps(resp), content_type="application/json")


#login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')


def class_report(request):
    if request.method == 'GET':
        class_id = request.GET.get('class_id')
        subject_id = request.GET.get('subject_id')
        class_obj = Class.objects.get(pk=class_id)
        active_class_obj = ActiveClass.objects.get(assigned_class=class_obj)
        students = ClassStudent.objects.filter(classIns=active_class_obj)
        subject = None
        if subject_id:
            subject = Subject.objects.get(pk=subject_id)
            students = students.filter(classIns__assigned_subject=subject)
            grade_points = students.values('mark').annotate(count=Count('id')).order_by('mark')
            total_students = students.count()
            passing_students = students.filter(mark__gte='33').count()
            passing_percentage = (passing_students / total_students) * 100 if total_students else 0
            grade_data = []
            for grade_point in grade_points:
                grade_data.append({
                    'grade': ClassStudent.get_grade_from_point(grade_point['mark']),
                    'count': grade_point['count'],
                    'percentage': (grade_point['count'] / total_students) * 100
                })
            chart_data = json.dumps({
                'labels': [data['grade'] for data in grade_data],
                'datasets': [{
                    'data': [data['count'] for data in grade_data],
                    'backgroundColor': [
                        '#FF6384',
                        '#36A2EB',
                        '#FFCE56',
                        '#F7DC6F',
                        '#58D68D',
                        '#A569BD',
                        '#F5B7B1',
                    ]
                }]
            })
        else:
            total_students = students.count()
            passing_students = students.filter(mark__gte='33').count()
            passing_percentage = (passing_students / total_students) * 100 if total_students else 0
            subject_data = students.values('classIns__assigned_subject').annotate(count=Count('id'))
            chart_data = json.dumps({
                'labels': [data['classIns__assigned_subject__name'] for data in subject_data],
                'datasets': [{
                    'data': [data['count'] for data in subject_data],
                    'backgroundColor': [
                        '#FF6384',
                        '#36A2EB',
                        '#FFCE56',
                        '#F7DC6F',
                        '#58D68D',
                        '#A569BD',
                        '#F5B7B1',
                    ]
                }]
            })
        context = {
            'class_obj': class_obj,
            'subject': subject,
            'total_students': total_students,
            'passing_students': passing_students,
            'passing_percentage': passing_percentage,
            'chart_data': chart_data,
        }
        return render(request, 'class_report.html', context)


def class_subjects_view(request):
    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        subject_id = request.POST.get('subject_id')
        students = ClassStudent.objects.filter(classIns__assigned_class__id=class_id)
        if subject_id:
            students = students.filter(classIns__assigned_subject__id=subject_id)
        total_students = students.count()
        passed_students = students.filter(mark__gte=33).count()
        passing_percentage = round(passed_students / total_students * 100, 2) if total_students != 0 else 0
        grades = {
            'A+': students.filter(mark__gte=80).count(),
            'A': students.filter(mark__gte=70, mark__lt=80).count(),
            'B': students.filter(mark__gte=60, mark__lt=70).count(),
            'C': students.filter(mark__gte=50, mark__lt=60).count(),
            'D': students.filter(mark__gte=40, mark__lt=50).count(),
            'E': students.filter(mark__gte=33, mark__lt=40).count(),
            'F': students.filter(mark__lt=33).count(),
        }
        grade_percentage = {grade: round(grades[grade] / total_students * 100, 2) if total_students != 0 else 0 for grade in grades}

        context = {
            'class_id': class_id,
            'subject_id': subject_id,
            'total_students': total_students,
            'passed_students': passed_students,
            'passing_percentage': passing_percentage,
            'grades': grades,
            'grade_percentage': grade_percentage,
        }
        return render(request, 'class_report.html', context)

    classes = Class.objects.all()
    subjects = Subject.objects.all()
    context = {'classes': classes, 'subjects': subjects}
    return render(request, 'class_report.html', context)


def class_subject_results(request):
    class_list = Class.objects.all()
    subject_list = Subject.objects.all()
    selected_class = request.GET.get('class')
    selected_subject = request.GET.get('subject')

    if selected_class:
        class_obj = Class.objects.get(id=selected_class)
        if selected_subject:
            subject_obj = Subject.objects.get(id=selected_subject)
            class_students = ClassStudent.objects.filter(classIns__assigned_class=class_obj, classIns__assigned_subject=subject_obj)
            total_students = class_students.count()
            grade_points = [student.get_grade_point() for student in class_students]
            grade_count = {
                'A+': grade_points.count(5.00),
                'A': grade_points.count(4.00),
                'A-': grade_points.count(3.50),
                'B': grade_points.count(3.25),
                'C': grade_points.count(2.00),
                'D': grade_points.count(1.00),
                'F': grade_points.count(0.00),
            }
            passing_students = ClassStudent.objects.filter(classIns__assigned_class=class_obj, classIns__assigned_subject=subject_obj, mark__gte=33).count()
            passing_percentage = (passing_students / total_students) * 100
            context = {
                'class_list': class_list,
                'subject_list': subject_list,
                'selected_class': selected_class,
                'selected_subject': selected_subject,
                'grade_count': grade_count,
                'passing_percentage': passing_percentage,
            }
        else:
            class_subjects = Subject.objects.filter(level=class_obj)
            subject_results = []
            for subject in class_subjects:
                subject_students = ClassStudent.objects.filter(classIns__assigned_class=class_obj, classIns__assigned_subject=subject)
                total_students = subject_students.count()
                if total_students > 0:
                    passing_students = subject_students.filter(mark__gte=33).count()
                    passing_percentage = (passing_students / total_students) * 100
                    subject_results.append({
                        'subject_name': subject.name,
                        'passing_percentage': passing_percentage,
                        'passing_students': passing_students,
                    })
            context = {
                'class_list': class_list,
                'subject_list': subject_list,
                'selected_class': selected_class,
                'subject_results': subject_results,
            }
    else:
        context = {
            'class_list': class_list,
            'subject_list': subject_list,
        }
    return render(request, 'class_subject_result.html', context)


def report(request):
    context = {}
    context['page'] = 'report'
    context['page_title'] = 'Report'

    request_data = request.GET
    check_class = request_data.get("check_class")
    check_subject = request_data.get("check_subject")

    _class = Class.objects.all()
    subject = Subject.objects.all()

    if check_class != "All" and check_subject == "All":
        class_obj = Class.objects.get(id=check_class)
        class_students = ClassStudent.objects.filter(classIns__assigned_class=class_obj.id).values('classIns__assigned_class__name', 'subject__name').annotate(pass_count=Count('id', filter=Q(mark__gte=33)), total_count=Count('id')).order_by('subject__name')

        for student in class_students:
            if student['total_count'] > 0:
                student['percent'] = round(student['pass_count'] / student['total_count'] * 100, 2)
            else:
                student['percent'] = 0

        context['class_students'] = class_students

    if check_class != "All" and check_subject != "All":
        class_student = ClassStudent.objects.filter(
            assigned_class=check_class,
            subject=check_subject
        ).annotate(
            total_students=Count('student'),
            total_grade_point=Sum('mark')
        )
        context['class_stu'] = class_student

    context['class'] = _class
    context['subject'] = subject

    return render(request, 'report/report.html', context)


def individual_report(request):
    context = {}
    context['page'] = 'individual_report'
    context['page_title'] = 'Individual Report'

    request_data = request.GET
    check_student = request_data.get("check_student")

    student = Student.objects.all()

    result = ClassStudent.objects.filter(student=check_student)

    context['student'] = student
    context['result'] = result

    return render(request, 'report/individual_result.html', context)




