from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=20, null=False,blank=False)

    author = models.CharField(max_length=15, null=False, blank=False)

    class Meta:
        verbose_name = "წიგნი"
        verbose_name_plural = "წიგნები"