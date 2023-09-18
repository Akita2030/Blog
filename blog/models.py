from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length = 128)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
