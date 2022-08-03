from django.db import models

class Message(models.Model):
    nama = models.CharField(max_length=100,default="")
    nim = models.IntegerField(default=0)
    message = models.TextField()

    def __str__(self):
        return self.name
