from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from .models import User, Note

# Create your views here.
def is_ajax(request):
  return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def login(request):
    login_template = loader.get_template('pyapp/login.html')
    index_template = loader.get_template('pyapp/index.html')
    context = {'title':'Nuevo Usuario'}
    if 'logged_in'not in request.session:
        return HttpResponse(login_template.render(context, request))
    else:
        return HttpResponse(index_template.render(context, request))
def index(request):
    usuarios = User.objects.order_by('id')
    template = loader.get_template('pyapp/index.html')
    context = {'usuarios': usuarios}
    return HttpResponse(template.render(context, request))
def ajax_test(request):
    message="not ajax"
    if is_ajax(request=request):
      new_note = {
        'title':request.POST.get('noteTitle'),
        'body':request.POST.get('noteBody')
      }
    return JsonResponse(new_note)
def register(request):
    template = loader.get_template('pyapp/register.html')
    context = {'title':'Nuevo Usuario'}
    return HttpResponse(template.render(context, request))
def register_action(request):
    try:
        nuevoUsuario = User(username=request.POST['username'], password=request.POST['password'], fechaCreacion=timezone.now())
        nuevoUsuario.save()
    except (KeyError):
        return HttpResponseRedirect(reverse('pyapp:registrar', args=()))
    else:
        return HttpResponseRedirect(reverse('pyapp:index', args=()))
def login_attempt(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    try:
        tmp_Usr = User.objects.get(username = uname)
        if tmp_Usr.username == uname and tmp_Usr.password == pwd:
            request.session['logged_in']=uname
            request.session.set_expiry(0)
            return HttpResponseRedirect(reverse('pyapp:index', args=()))
        else:
            return HttpResponse('<script>alert("Revisa los datos introducidos");</script>')
    except:
        return HttpResponse('<script>alert("Revisa los datos");</script>')
    else:
        return render(request, 'pyapp/login.html')
def logout_action(request):
    del request.session['logged_in']
    return HttpResponseRedirect(reverse('pyapp:index', args=()))
def my_notes(request):
    notes = Note.objects.order_by('id')
    template = loader.get_template('pyapp/my_notes.html')
    context = {'notes':notes}
#    return HttpResponseRedirect(reverse('pyapp:my_notes', args=()))
    return HttpResponse(template.render(context, request))

