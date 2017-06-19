# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index (request):
    return HttpResponse("<h>this is the books homepage22</h>")


def detail (request,book_id):
    return HttpResponse("<h2>details for book id:" + str(book_id)+"</h2>")


