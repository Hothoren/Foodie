#! usr/bin/python

#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

# Create your views here.
def home(request):
    return render(
        request,
        'takeout/index.html',
    )
def about(request):
    return render(
        request,
        'takeout/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'HHH.',
        })
    )
def contact(request):
    return render(
        request,
        'takeout/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'HHH.',
        })
    )
