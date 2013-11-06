# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

def hello(request):
    name = "Mike"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Mike"
    template = loader.get_template('hello.html')
    html = template.render(RequestContext(request,{'name':name})) # request gets passed a dict with the name and variable
    return HttpResponse(html)
