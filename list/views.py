from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import List, Check_list

# Create your views here.

def home(request):
    return HttpResponse("Welcome!")


def create(request):
    return render(request, 'list/create.html',{})


def add(request):
    s = get_object_or_404(request)
    context = {
        'title': s.title,
        'description': s.description,
    }

    context.save()


def add_check(request):
    pass
