
from django.db import models

from core.models import AbstractTimeStamp
from users.models import User


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.hashtag

    class Meta:
        db_table = 'hashtag'

class Article(AbstractTimeStamp):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=300, blank=False)
    content = models.TextField(max_length=1000)
    hashtags = models.ManyToManyField(Hashtag, related_name='articles')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    view = models.PositiveIntegerField(default=0)
    delete_flag = models.BooleanField(default=False)

    class Meta:
        db_table = 'article'

    def delete_on(self):
        self.delete_flag = not self.delete_flag
        self.save()


    def __str__(self):
        return f'user:{self.user.name},title:{self.title},hashtags:{self.hashtags}'



