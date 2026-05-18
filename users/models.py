from django.db import models


class Enrollment(models.Model):
    student = models.ForeignKey(
        'students.Sudent',
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    course = models.ForeignKey(
        'academics.Course',
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    term = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.course}"
