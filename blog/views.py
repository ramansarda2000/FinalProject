from django.http import HttpResponse
from blog.models import Blog
from django.template import loader
from django.shortcuts import render

def index(request):
	latest_blog_list = Blog.objects.order_by('-created')[:5]
	context = {'latest_blog_list': latest_blog_list, }
	return render(request, 'blog/index.html', context)

def info(request, Blog_id):
    try:
        blog = Blog.objects.get(pk=Blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, 'blog/info.html', {'Blog': blog.body})
