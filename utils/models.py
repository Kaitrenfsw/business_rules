from django.db import models


class DateConversion(models.Model):
    date = models.CharField(null=False, max_length=15)
    week = models.IntegerField(null=False)
    sunday_date = models.CharField(null=False, max_length=15, default='00/00/0000')

