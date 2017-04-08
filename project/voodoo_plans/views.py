# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'home.html', {})

def itnrsub(request):
    return render(request, 'submit.html', {})

def algo_results(request):
    return render(request, 'itinerary_template.html', {})
