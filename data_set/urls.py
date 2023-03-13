from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.report, name="home-page"),
    path('class',views.class_list,name='class-page'),
    path('manage_class',views.manage_class,name='manage-class'),
    path('manage_class/<int:pk>',views.manage_class,name='edit-class'),
    path('save_class',views.save_class,name='save-class'),
    path('delete_class',views.delete_class,name='delete-class'),
    # subjects
    path('subject',views.subject,name='subject-page'),
    path('manage_subject',views.manage_subject,name='manage-subject'),
    path('manage_subject/<int:pk>',views.manage_subject,name='edit-subject'),
    path('save_subject',views.save_subject,name='save-subject'),
    path('delete_subject',views.delete_subject,name='delete-subject'),
    # students
    path('student',views.student,name='student-page'),
    path('manage_student',views.manage_student,name='manage-student'),
    path('view_student/<int:pk>',views.view_student,name='view-student'),
    path(r'manage_student/<int:pk>',views.manage_student,name='edit-student'),
    path('save_student',views.save_student,name='save-student'),
    path('delete_student',views.delete_student,name='delete-student'),
    # teacher
    path('teacher',views.teacher,name='teacher-page'),
    path('manage_teacher',views.manage_teacher,name='manage-teacher'),
    path('view_teacher/<int:pk>',views.view_teacher,name='view-teacher'),
    path('manage_teacher/<int:pk>',views.manage_teacher,name='edit-teacher'),
    path('save_teacher',views.save_teacher,name='save-teacher'),
    path('delete_teacher',views.delete_teacher,name='delete-teacher'),
    # assigned class
    path('assigned_class',views.active_class,name='active-class-page'),
    path('manage_assigned_class',views.manage_active_class,name='manage-active-class'),
    path('manage_assigned_class/<int:pk>',views.manage_active_class,name='edit-active-class'),
    path('view_assigned_class/<int:pk>',views.view_active_class,name='view-class-page'),
    path('save_assigned_class',views.save_active_class,name='save-active-class'),
    path('delete_assigned_class',views.delete_active_class,name='delete-active-class'),
    path('view_assigned_student/<int:pk>',views.view_assigned_student,name='view-assigned-student'),
    # class student
    path('assigned_class_result',views.active_class_result,name='active-class-result-page'),
    path('manage_class_student/<int:classPK>',views.manage_class_student,name='class-student-modal'),
    path('save_class_student/',views.save_class_student,name='save-class-student'),
    path('delete_class_student',views.delete_class_student,name='delete-class-student'),
    # authenticate
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('login',auth_views.LoginView.as_view(template_name="authorize/login.html",redirect_authenticated_user = True),name='login'),
    path('userlogin', views.login_user, name="login-user"),
    path('logout',views.logoutuser,name='logout'),
    path('class-report/', views.class_report, name='class_report'),
    #path('subject-report/', views.subject_report, name='subject_report'),
    # path('class-subjects/', views.class_subjects_view, name='class_subjects'),
    # path('class_subject_results/', views.class_subject_results, name='class_subject_results'),
    path('report', views.report, name="report"),
    path('individual_report', views.individual_report, name="individual-report"),
]