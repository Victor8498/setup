# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    #request="Just checking to see if it works, apparently it does!"
    return render(request,'random_word/index.html')

def random(request):
    if 'number' in request.session:
        request.session['number'] += 1
    else:
        request.session['number'] = 1
    word = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v','w','x','y','z']
    for times in range (0, 14):
       word = word + str(random.choice(letters))
    words = {
        'random_word': word,
    }
    return render(request, 'random_word/index.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')
#    return render(request,'random_word/index.html')