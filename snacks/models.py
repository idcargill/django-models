from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model


class Snack(models.Model):
  name = models.CharField(max_length=64)
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  description = models.TextField(max_length=200, default='')

  def __str__(self):
    return self.name
