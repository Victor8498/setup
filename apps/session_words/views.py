# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def process(request, methods=['POST']):
    if request.method == "POST":    #starting from here we get the word we write to  on the other side.
        words = request.POST['wordy']
        request.session['word'] = words 
        wordz = request.session['word'] #ending here
        print "++++++++++++++++++++++++++++++++++"

    if  request.method == "POST": # i grab the name of the color and the idea is to set it to class on the html side but it is not working
        request.POST['color']
        request.session['color'] = request.POST['color']
        print "****************************************"



#        big = request.POST['big']
#        request.session['big'] = big
#        bigz = request.session['big']
#        bigzz = wordz
        return render(request,'index.html')


def clear(request):
    return redirect('/')

