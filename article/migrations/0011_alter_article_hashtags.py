# Generated by Django 4.0.6 on 2022-07-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_alter_hashtag_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hashtags',
            field=models.ManyToManyField(related_name='articles', to='article.hashtag'),
        ),
    ]
