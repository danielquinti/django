from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Message
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
def message(request):
    return HttpResponse(Message.objects.all().order_by("pub_date")[0].__str__())