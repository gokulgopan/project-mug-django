from django.shortcuts import render
from django.http import HttpResponse
from .models import Update
from . import forms
from .forms import UpdateForm

# Create your views here.

def index(request):
    latest_updates_list = Update.objects.order_by('-date_pub')[:5]
    date_dict = {'access_records':latest_updates_list}
    #output = ', ' .join([p.title for p in latest_updates_list]) 
    #return HttpResponse(output)
    return render (request,'updates/index.html', context=date_dict)

def update_add(request):
    form = UpdateForm()
    #if form.is_valid():
    #    form.save()
    return render(request, 'updates/add-update.html', {'form': form})

def update_detail(request, id):
    #return HttpResponse(id)
    updates = Update.objects.get(id=id)
    return render(request, 'updates/update_detail.html', {'updates':updates})