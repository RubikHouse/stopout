from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    # ex: /polls/5/
    # path('', views.index, name='index'),
    path(r'schools/$', views.school_list, name='school-list'),
    path(r'students/$', views.student_list, name='student-list'),
    path('<int:school_id>/', views.school_detail, name='school-detail'),
    path('<int:student_id>/', views.student_detail, name='student-detail'),

]