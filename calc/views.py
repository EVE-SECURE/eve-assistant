from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from marketApi import *


# Create your views here.

def index(request):
	list = getMinerals()
	template = loader.get_template('calc/index.tmp')
	context = RequestContext(request, {
		'list': list,
	})
	return HttpResponse(template.render(context))
