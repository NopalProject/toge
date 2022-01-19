from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import User

# Create your views here.
def login(request):
        return HttpResponse(f"1+1={11}")
def index(request):
	usuarios = User.objects.order_by('id')[:5]
	template = loader.get_template('login/index.html')
	context = {'usuarios': usuarios}
        #return render(request, 'login/index.html', context)
	return HttpResponse(template.render(context, request))
def userlist(request, num):
        return HttpResponse("Total de usuario %s." % num)
