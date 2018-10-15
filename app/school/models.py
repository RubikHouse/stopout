from django.db import models

# Create your models here.
from django.db import models

__all__= (
    'School',
    'Student',
)


class School(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    close_friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name


