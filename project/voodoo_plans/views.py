# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
sys.path.insert(0, './backend')

import autocomplete

def index(request):
    return HttpResponse("Hello, world. You're at the voodoo_plans index.")
