from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Blog

def blog(request):
  blog = Blog.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'blog': blog,
  }
  return JsonResponse(list(blog), safe=False)
  
def details(request, id):
  blog = Blog.objects.all().values()
  template = loader.get_template('details.html')
  context = {
    'blog': blog,
  }
  return HttpResponse(template.render(context, request))

def index(request):
  blog = Blog.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'blog': blog,
    'title': "Home",
    'set': 1,
    }
  return HttpResponse(template.render(context, request))