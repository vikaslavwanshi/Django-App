from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home page'), # To display Student and course details on main page , on <baseURL> landing page
    path('students/', views.studentList, name='student_list'), # Student List view
    path('courses/', views.courseList, name='course_list'), # All Course List view
    path('courses/<int:course_id>/', views.courseDetails, name='course_detail') # single course view with details 
]