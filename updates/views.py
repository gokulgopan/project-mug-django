from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Update
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    latest_updates_list = Update.objects.order_by('-date_pub')[:5]
    date_dict = {'access_records':latest_updates_list}
    #output = ', ' .join([p.title for p in latest_updates_list]) 
    #return HttpResponse(output)
    return render (request,'updates/index.html', context=date_dict)

@login_required(login_url="/accounts/login/")
def create_view(request):
    if request.method == 'POST':
        form = forms.CreateUpdate(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('updates:index')
    else:
        form = forms.CreateUpdate()
    return render(request, 'updates/create.html', {'form':form})

def update_detail(request, id):
    #return HttpResponse(id)
    updates = Update.objects.get(id=id)
    return render(request, 'updates/update_detail.html', {'updates':updates})