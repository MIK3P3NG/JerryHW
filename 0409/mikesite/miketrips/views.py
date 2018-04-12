from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("hello mom I'm here")

def fuck(request):
	return HttpResponse("hello dad I'm here")