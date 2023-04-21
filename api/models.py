from django.db import models

# Create your models here.

class PostIt(models.Model):
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.body[0:50]