from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 128)
    text = models.TextField()
    pub_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now())


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.title
    

    def get_absolute_url(self):
        return reverse('post_detail',
                   args=[str(self.id)]
                   )