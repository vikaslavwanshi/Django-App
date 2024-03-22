from django.utils import timezone
from django.db import models

class Courses(models.Model):
    capacity = models.IntegerField() #Size (Max number of student)
    courseName = models.CharField(max_length=100) #course names
    nameOfCourseCordinator = models.CharField(max_length=100) #  Name of course cordinators
    def __str__(self):
        return self.courseName

class Students(models.Model):
    name = models.CharField(max_length=100)
    emailAddress = models.EmailField(max_length=255)
    studentId = models.IntegerField(unique=True)
    dob = models.DateField(max_length=8)
    courseEnrolled = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def total_student_in_course(self):
        return Students.objects.filter(courseEnrolled=self.courseEnrolled).count()