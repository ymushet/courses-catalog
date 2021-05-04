from django.core.validators import MinValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    lectures = models.PositiveSmallIntegerField(default=1,
                                                validators=[
                                                    MinValueValidator(1)
                                                ])

    def __str__(self):
        return f'{self.name} course has {self.lectures} lectures'
