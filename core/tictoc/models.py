from django.db import models

# Create your models here.
class tictocModel(models.Model):
    player = models.CharField(max_length=100, blank=True, null=True)
    action = models.CharField(max_length=100, blank=True, null=True)
    board = models.CharField(max_length=100, blank=True, null=True)
    winner = models.CharField(max_length=100, blank=True, null=True)
    terminal = models.BooleanField(max_length=100, blank=True, null=True)
    move = models.CharField(max_length=100, blank=True, null=True)