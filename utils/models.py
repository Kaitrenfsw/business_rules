from django.db import models


class DateConversion(models.Model):
    date = models.DateField()
    week = models.IntegerField(null=False)
    sunday_date = models.DateField()

