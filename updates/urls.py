from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url
from .models import Update
from .views import update_add
from .views import update_detail


app_name = 'updates'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', update_add),
    url(r'^(?P<id>[\w]+)/$',update_detail, name="detail"),
]
