from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root path shows homepage
    path('admissions/', views.admissions_student, name ='admissions_student'),
    path('apply/student/', views.apply_student, name ='apply_student'),
    path('teachers/', views.teacher_landing, name='teacher_landing'),
    path('teachers/apply/', views.apply_teacher, name='apply_teacher'),
    path('campus-tour/', views.campus_tour, name='campus_tour'),
]
