from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.subject

