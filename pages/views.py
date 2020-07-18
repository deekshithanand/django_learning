from django.shortcuts import render
from django.shortcuts import render
from django.http import request,response,HttpResponse
from listings.models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.all()
    context = {'listings' : listings}
    return render(request,'index.html',context=context)

def about(request):
    return render(request,'about.html')
    