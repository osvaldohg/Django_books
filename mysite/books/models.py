# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return HttpResponse("<h>this is the books homepage</h>")


class Book (models.Model):
    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + '-' + self.author

    name= models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    book_image=models.CharField(max_length=1000)






