from django.db import models


class UserPreferences(models.Model):
    destination = models.CharField(max_length=100)
    budget = models.IntegerField()
    interests = models.TextField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

