from django.http import HttpResponse, Http404
from blog.models import Blog
from django.template import loader
from django.shortcuts import render

def index(request):
	template = loader.get_template('FinalProject/index.html')
	return render(request, 'FinalProject/index.html', context=None)
