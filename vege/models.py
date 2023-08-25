from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reciepe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    reciepe_name = models.CharField(max_length=100)
    reciepe_description = models.TextField()
    reciepe_image = models.ImageField(upload_to="reciepe")


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']

#this is studentId table Associated wit student table
class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
#Subjects
class Subject(models.Model):
    subject_name=models.CharField(max_length=100)
    
    
    
    
    

# this is Student table
class Student(models.Model):
    department = models.ForeignKey(
        Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(
        StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = "student"
        
 
 #Subject marks of student       
class SubjectMarks(models.Model):
    student=models.ForeignKey(Student,related_name="studentmarks",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.student.student_name}{self.subject.subject_name}'
    
    class Meta:
        unique_together=['student','subject']
