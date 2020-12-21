# -*- coding: utf-8 -*-from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Backend_Interpreter(models.Model):
    file_name = models.CharField("File Name", max_length=255)


    def __str__(self):
        return self.first_name
