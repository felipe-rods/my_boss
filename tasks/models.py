from django.db import models
from django.contrib.auth.models import User


PRIORITY_CHOICES = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='tasks',
    )
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title
