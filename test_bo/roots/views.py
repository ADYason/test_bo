import math
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .models import Roots
from .forms import RootsForm


class RootsView(ListView):
    model = Roots
    template_name = 'roots/roots_list.html'
    context_object_name = 'roots'


def index(request):
    template = 'roots/index.html'
    context = {}
    return render(request, template, context)


def roots_create(request):
    form = RootsForm(request.POST or None)
    if form.is_valid():
        equasion = form.save(commit=False)
        a, b, c = equasion.a, equasion.b, equasion.c
        d = (b**2) - (4*a*c)
        if d < 0:
            equasion.roots = 'корней нет'
        elif d == 0:
            equasion.roots = (-b)/(2*a)
        else:
            equasion.roots = (-b+math.sqrt(d))/2*a, (-b-math.sqrt(d))/(2*a)
        equasion.save()
        return redirect('roots:list')
    return render(request, 'roots/roots_form.html', {'form': form})
