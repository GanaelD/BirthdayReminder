from django.db import models


class Birthday(models.Model):
    person_name = models.CharField(max_length=20)
    month = models.IntegerField()
    day = models.IntegerField()
