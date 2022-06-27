from operator import mod
from django.db import models


class Record(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)