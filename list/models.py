from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        tdc = self.title + self.description
        return tdc

class Check_list(models.Model):
    list = models.ForeignKey(List)
    check_list_text = models.CharField(max_length=200)