from django.db import models
#from django import forms

class Stage(models.Model):
    STAGES = (('FG','first grade'),('SG','second grade'),('TG','third grade'),)

    sstage = models.CharField(max_length=2,choices=STAGES)
    def __str__(self):
        return self.sstage + '-' + str(self.id)

# Create your models here.

class Student(models.Model):
    sname = models.CharField(verbose_name="Student Name", max_length=50)
    sage = models.IntegerField(verbose_name="Student Age", null = True)
    stage = models.ForeignKey(Stage, related_name='Stage', on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(verbose_name="Student Password", max_length=128, null=False, blank=False)

    def __str__(self):
        return self.sname

