from django.core.validators import MinValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey('auth.User', related_name='courses', on_delete=models.CASCADE)
    start_at = models.DateTimeField(blank=False, null=False)
    end_at = models.DateTimeField(blank=False, null=False)
    lectures = models.PositiveSmallIntegerField(default=1,
                                                validators=[
                                                    MinValueValidator(1),
                                                ])

    class Meta:
        ordering = ('start_at',)

    def __str__(self):
        return f'{self.name} course has {self.lectures} lectures'
