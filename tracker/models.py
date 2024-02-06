from django.db import models

# Create your models here.

# A Django model corresponds to a table (entity). They are built using
# classes that extend the Django models.Model class.
class Course(models.Model):
    title = models.CharField(max_length=255)
    credits = models.IntegerField(default=4)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(null=True) # null=True means allowed to be NULL
    points = models.IntegerField(default=100)

    def __str__(self):
        return self.title
