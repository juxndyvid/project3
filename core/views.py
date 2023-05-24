from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    # return HttpResponse('vamos melos :D')
    return render(request, 'core/index.html')

def cerrar(request):
    logout(request)
    return redirect('/')