from .models import Topic, Entry
from  django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    """Return home page for learning logs"""
    return render(request,'index.html')

def topics(request):
    """Return Stored Topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'topics.html',context)

def topic(request):
    """Return Stored Topics and all its Entries."""
    topic = Topic.objects.all()
    entries = topic.entry_set.order_by('date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request,'topic.html',context)

def entries(request):
    """Return all Entries"""
    entries = Entry.objects.order_by('date_added')
    context = {'entries':entries}
    return render(request,'topics.html',context)

def about_us(request):
    """Return About Us Page"""
    return render(request,'about_us.html')

def contact_us(request):
    """Return Contact Us Page."""
    return render(request,'contact_us.html')