# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process(request, methods="POST"):
    if request.method == 'POST':
        #the type of item you want
        #Number of items you are purchasing
        NMBR1 = int(request.POST["number1"])
        NMBR2 = int(request.POST["number2"])
        NMBR3 = int(request.POST["number3"])
        NMBR4 = int(request.POST["number4"])

        NMBR = (NMBR1 + NMBR2 + NMBR3 + NMBR4)
        print NMBR
        request.session["NMBR"] = NMBR

        if len(request.POST["number1"]) > 0:
           TTL1 = NMBR1 * 19.99
        if len(request.POST["number2"]) > 0:
           TTL2 = NMBR2 * 29.99
        if len(request.POST["number3"]) > 0:
           TTL3 = NMBR3 * 4.99
        if len(request.POST["number4"]) > 0:
           TTL4 = NMBR4 * 49.99

        TTL = (TTL1 + TTL2 + TTL3 + TTL4)
        print TTL
        request.session["TTL"] = TTL
        
        return redirect('/checkout')

def checkout(request):
    return render(request, 'checkout.html')


#        ITM1 = int(request.POST["item1"])
#        ITM2 = int(request.POST["item2"])
#        ITM3 = int(request.POST["item3"])
#        ITM4 = int(request.POST["item4"])
#        
#        ITM = ((ITM1 * NMBR1) + (ITM2 * NMBR2) + (ITM3 * NMBR3) + (ITM4 * NMBR4))
#
#        print ITM
#        request.session["ITM"] = ITM