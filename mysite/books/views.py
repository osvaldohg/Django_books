# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    template_name='books/index.html'

    def get_queryset(self):
        return Book.objects.all()



class DetailView(generic.DetailView):
    model = Book
    template_name='books/detail.html'

class BookCreate(CreateView):
    model = Book
    fields = ['name','author','price','type','book_image']



