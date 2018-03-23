# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def process(request, methods=['POST']):
    if request.method == "POST":
        print "coldcoldcold"
        YN = request.POST['YN']
        LCTN = request.POST['LCTN']
        LNG = request.POST['LNG']
        CMNT = request.POST['CMNT']
        request.session['name'] = request.POST['YN']
        request.session['location'] = request.POST['LCTN'] 
        request.session['language'] = request.POST['LNG']
        request.session['comment'] = request.POST['CMNT']
        return redirect('/results')

def results(request):
    return render(request,'results.html', )