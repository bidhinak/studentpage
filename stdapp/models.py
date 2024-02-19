from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)

class student(models.Model):
    one=models.ForeignKey(Login,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=30)
    date_of_birth=models.DateField()
    phone_number=models.CharField(max_length=10)
    photo=models.FileField(upload_to="images/")

    def __str__(self):
        return self.student_name


class teacher(models.Model):
    two=models.ForeignKey(Login,on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=50)
    staff_id = models.IntegerField()
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)

class marksadd(models.Model):
    SUBJECTS = (
        ('CS', 'Computer science'),
        ('BCA', 'computer application'),
        ('FT', 'Food technology'),
        ('Physics', 'physics'),
        ('Maths', 'maths')
    )
    student_name=models.ForeignKey(student,on_delete=models.CASCADE)
    subject=models.CharField(max_length=30,choices=SUBJECTS)
    mark=models.IntegerField()

