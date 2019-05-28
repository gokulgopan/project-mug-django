from django.shortcuts import render
from django.http import HttpResponse
from .models import Update
# Create your views here.

def index(request):
    latest_updates_list = Update.objects.order_by('-date_pub')[:5]
    date_dict = {'access_records':latest_updates_list}
    #output = ', ' .join([p.title for p in latest_updates_list]) 
    #return HttpResponse(output)
    return render (request,'updates/index.html', context=date_dict)