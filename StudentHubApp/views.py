from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Courses, Students
import logging

# This Fucntion is created for Student List view
def studentList(request):
    # To capture all objects for each class
    students = Students.objects.all()

    return render(request, 'student_list.html', {
        'students': students})

# This Fucntion is created for course List view with course name and total student per course view.  --> course_list.html
def courseList(request):
    # To capture all objects for each class
    a = Courses.objects.all()
    return render(request, 'course_list.html', {
        'courses': a})

# To display single course view with complete course details 
# and to display total number of enrolled student in each course--> from course_details.html
def courseDetails(request, course_id):
    course = get_object_or_404(Courses, id=course_id)

    # To get the list of students enrolled in the course
    students_enrolled = Students.objects.filter(courseEnrolled=course)

    #Calculating total student enrolled in the course
    total_students_enrolled = students_enrolled.count()

    return render(request, 'course_details.html', {
        'course': course, 
        'students_enrolled': students_enrolled, 
        'total_students_enrolled': total_students_enrolled})

# This is combination of Student list and course List , which could be displayed on landing page . i.e, /app --> from index.html 
def index(request):
    return render(request, 'index.html')

def error_404(request, exception):
    return HttpResponse('ERR:404 - page is not found', status = 404)