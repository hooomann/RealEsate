from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices,intention
from .models import Listing
from django.contrib.auth.models import User
from realtors.models import Realtor
from django.contrib import messages
from .forms import PLForm
from django.contrib.auth.decorators import login_required

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(title__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)
      # print("1")

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      x=state_choices[state]
      queryset_list = queryset_list.filter(state__icontains=x)
      # print(state_choices[state])

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
# intention
  if 'intentions' in request.GET:
    intent = request.GET['intentions']
    if intent:
      x=intention[intent]
      queryset_list = queryset_list.filter(intention__iexact=x)
  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)
      print(type(price))
      print(price)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'intention':intention,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)

@login_required
def postlisting(request):
    form=PLForm()
    if request.method=='POST':
      
      form=PLForm(request.POST , request.FILES)
      print(request.POST)
      print(request.FILES)

      if form.is_valid():
        form.save()
        print(form.errors)
        messages.success(request,"Your Advertisement is Posted ")
        return redirect('index')
      else:
        print(form.errors,"forms errors")
        messages.error(request,"Please Fill All the Required fields")
        return redirect('postlisting')    
    else:
      form = PLForm()
      ins=list(Realtor.objects.values('name','id'))
      reals={}

      for i in ins:
        kv=i['name']
        ki=i['id']
        reals[ki]=kv

      print(reals)
      context={
        'state_choices': state_choices,
        'reals':reals,
        'intention':intention,
        'form':form
      }
      messages.info(request,"  * signifies required fields")
      return render(request,'listings/postlisting.html',context)