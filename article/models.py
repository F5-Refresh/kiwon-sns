from django.db import models

from core.models import AbstractTimeStamp


class Article(AbstractTimeStamp):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=300,blank=False)
    content = models.TextField(max_length=1000)
    hashtag = models.CharField(max_length=200)
    like = models.PositiveIntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    delete_flag = models.BooleanField(default=False)

    class Meta:
        db_table = 'article'

    def delete_on(self):
        self.delete_flag = not self.delete_flag
        self.save()


    def __str__(self):
        return f'user:{self.user.name},title:{self.title}'

