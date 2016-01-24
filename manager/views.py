from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world! You're at the manager index.")

def detail(request, questionID):
    return HttpResponse("You're looking at question %s." % questionID)

def results(request, questionID):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionID)

def vote(request, questionID):
    return HttpResponse("You're voting on question %s." % questionID)


