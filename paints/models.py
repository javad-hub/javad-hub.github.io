from django.db import models
from accounts.models import CustomUser
from django.conf import settings
from django.urls import reverse
# Create your models here.

User = settings.AUTH_USER_MODEL

class Paint(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=225)
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='paints')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name


class Comment(models.Model):
    paint = models.ForeignKey(Paint, related_name='comments', on_delete=models.CASCADE , default="" ,editable=True )
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ('%s - %s') %(self.paint.name, self.name)

    def get_absolute_url(self):
        return reverse('comment')


