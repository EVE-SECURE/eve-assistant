from django.shortcuts import render
from django.http import HttpResponse
from marketApi import *

# Create your views here.

def index(request):
	s = ""
	for o in getMinerals():
		s += o['name'] + ':' + o['price'] + ','
	return HttpResponse(s)
