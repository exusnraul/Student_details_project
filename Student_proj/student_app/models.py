from django.db import models
from django.urls import reverse

# Create your models here.


class Student_details(models.Model):

    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    message = models.CharField(max_length=250)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student_app:student_list")
    
    