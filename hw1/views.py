from django.shortcuts import render
from django.http import *
from django import template
from django.shortcuts import render_to_response
from django.http import HttpResponse
import re
import collections




def word_frequency(request,file):
    text = open("C:\Users\enesbasarir\Desktop\Faculty\sixthTerm\Software\hw1\hw1\%s" %file, "r")
    words = re.findall('\w+', text.read().lower())
    frequency = collections.Counter(words)
    html = "<html><body>" \
           "<h1>Histogram</h1> ",\
           "<p>The name of the file is: " ,file, "</p> The counts of word in given text %s" \
                                                                       "" \
                                                                       "</body></html>" %frequency

    return HttpResponse(html)