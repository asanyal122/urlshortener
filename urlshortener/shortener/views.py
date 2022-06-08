from django.shortcuts import render,redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def get_existing(url):
    existing_url=None
    try:
        existing_url=Url.objects.get(link=url)
    except Url.DoesNotExist:
        existing_url=None

    return existing_url

def create(request):
    if request.method=='POST':
        url=request.POST['link']
        uid=str(uuid.uuid4())[:5]
        new_url=get_existing(url)
        
        if(new_url is None):
            new_url=Url(link=url,uid=uid)
            new_url.save()
        return HttpResponse(new_url.uid)

def go(request,pk):
    url=Url.objects.get(uid=pk)
    return redirect(url.link)