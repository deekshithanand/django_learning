from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator
# Create your views here.
def listings(request):
    listings = Listing.objects.order_by('list_date').filter(is_published=True)
    paginator = Paginator(listings, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'listings' : page_obj}
    return render(request, 'listings.html',context)

def listing(request,listing_id):
    return render(request,'listing.html')

def search(request):
    return render(request,'search.html')

