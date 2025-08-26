from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # This links the subject to a user
    name = models.CharField(max_length=100)
    total_time = models.PositiveIntegerField(default=0)  # Total time spent on this subject (in seconds or minutes)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Links chapter to a subject
    name = models.CharField(max_length=100)
    time_studied = models.PositiveIntegerField(default=0)  # Time spent on this chapter
    notes = models.TextField(blank=True, default='')  

    def __str__(self):
        return self.name