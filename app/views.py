from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def this_is_first(request):
    return HttpResponse("this_is_first")