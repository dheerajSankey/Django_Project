from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hello django home page")
  return  render(request,'websites/index.htm')


def about(request):
    return HttpResponse("hello django about page")