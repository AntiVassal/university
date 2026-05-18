from django.db import models


class Major(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        'students.Department',
        on_delete=models.CASCADE,
        related_name='courses',
    )
    credits = models.IntegerField()

    def __str__(self):
        return self.name
