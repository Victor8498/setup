# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    print "At index"
    users = User.objects.all()
    user = User.objects.get(id=1)
    return render(request, 'index.html')