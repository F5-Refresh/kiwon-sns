from django.db import models

class AbstractTimeStamp(models.Model):
    created = models. DateTimeField('Created Time',auto_now_add=True)
    updated = models. DateTimeField('Updated Time',auto_now=True)

    class Meta:
        abstract = True