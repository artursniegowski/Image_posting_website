from tkinter import Widget
from django.contrib import admin
from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length=140)
    post_time = models.DateTimeField(default=timezone.now)
    image = ImageField()

    def __str__(self) -> str:
        return self.text