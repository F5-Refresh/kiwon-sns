# Generated by Django 4.0.6 on 2022-07-23 18:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0005_remove_article_like_article_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hashtag',
        ),
        migrations.AddField(
            model_name='article',
            name='hashtag',
            field=models.ManyToManyField(max_length=200, related_name='hashtag', to=settings.AUTH_USER_MODEL),
        ),
    ]
