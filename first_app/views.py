from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello World")


def inputInt(request, num):
    if(num%2==0):
        output="%s is an even number." % num
    else:
        output="%s is an odd number." % num
    return HttpResponse(output)

