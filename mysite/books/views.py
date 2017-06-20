# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

def index (request):
    all_books=Book.objects.all()
    html=''
    for book in all_books:
        url='/books/'+str(book.id)+'/'
        html+='<a href="'+ url+'">'+str(book.name)+'</a><br>'


    return HttpResponse(html)


def detail (request,book_id):
    return HttpResponse("<h2>details for book id:" + str(book_id)+"</h2>")


