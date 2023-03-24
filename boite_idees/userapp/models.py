from django.db import models
from django.contrib.auth.models import User

class Idea(models.Model):
    formulation = models.CharField(max_length=100)
    detail = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Voter(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    vote = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('voter', 'idea')
