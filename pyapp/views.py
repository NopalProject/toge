from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import User

# Create your views here.
def login(request):
	template = loader.get_template('pyapp/login.html')
	context = {'titulos':'login'}
	return HttpResponse(template.render(context, request))
#	return HttpResponse('si')
def index(request):
	usuarios = User.objects.order_by('id')[:5]
	template = loader.get_template('pyapp/index.html')
	context = {'usuarios': usuarios}
        #return render(request, 'login/index.html', context)
	return HttpResponse(template.render(context, request))
def userlist(request, num):
        return HttpResponse("Total de usuario %s." % num)
