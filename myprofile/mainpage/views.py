from django.http import HttpResponse
from django.template import loader

def homepage(request):
  a='charalambos'
  template = loader.get_template('homepage.html')
  context = {
    'mylogo':a,
  }
  return HttpResponse(template.render(context, request))
