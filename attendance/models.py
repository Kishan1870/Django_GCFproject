from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField()  # True = Present, False = Absent


    def __str__(self):
        return f"{self.student} - {self.subject} - {self.date}"
