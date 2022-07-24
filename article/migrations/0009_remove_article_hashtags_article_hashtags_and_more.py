# Generated by Django 4.0.6 on 2022-07-24 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_hashtag_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hashtags',
        ),
        migrations.AddField(
            model_name='article',
            name='hashtags',
            field=models.ManyToManyField(blank=True, max_length=200, related_name='articles', to='article.hashtag'),
        ),
        migrations.RemoveField(
            model_name='hashtag',
            name='hashtag',
        ),
        migrations.AddField(
            model_name='hashtag',
            name='hashtag',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterModelTable(
            name='hashtag',
            table=None,
        ),
    ]