from django.db import models
from event.models import User


class SuggestionEvent(models.Model):
    use_in_migrations = True
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    classification = models.CharField(max_length=30)
    title = models.CharField(max_length=50, blank=True)
    start = models.CharField(max_length=25,  blank=True)
    end = models.CharField(max_length=25,  blank=True)
    location = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.suggestion_id}, {self.title}'

    class Meta:
        db_table = 'suggestions'

