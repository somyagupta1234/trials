from django.http import HttpResponse
from django.template import loader
from .models import Student,Teacher

def testing(request):
  mydata = Student.objects.all().values()
  template = loader.get_template('template1.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))