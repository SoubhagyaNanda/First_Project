from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
    return HttpResponse('<h1>This is a Heading</h1>')

def second_sample(request):
    return HttpResponse('<marquee><i><h1>This is a infanite scroll bar</h1></i></marquee>')