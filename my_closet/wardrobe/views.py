from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ItemForm
# Create your views here.

def starting_page(request):
    return render(request, 'wardrobe/index.html')

def form(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
    else:
        form = ItemForm()
   
    return render(request, 'wardrobe/form.html', {"form": form})