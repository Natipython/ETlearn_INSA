
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=225)
    course_desc = models.TextField()
    
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name


class Lesson(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=225)
    lesson_description = models.TextField()
    lesson_content = models.TextField()
    lesson_duration = models.DurationField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson_title
    
class Contact(models.Model):
    gmail = models.EmailField()
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def str(self):
        return self.name