import random
from django.shortcuts import render, redirect
from django.views.generic.list import ListView


from .models import Items
from .forms import ItemsForm


class ItemsView(ListView):
    model = Items
    template_name = 'items/roots_list.html'
    context_object_name = 'items'


def items_create(request):
    form = ItemsForm(request.POST or None)
    if form.is_valid():
        equasion = form.save(commit=False)
        pick = equasion.pick
        clrs = ('красный', 'зелёный', 'зелёный', 'синий', 'синий', 'синий', 'синий')
        ar = random.choices(clrs, k=100)
        equasion.result = ar[pick]
        equasion.save()
        return redirect('items:list')
    return render(request, 'items/items_form.html', {'form': form})
