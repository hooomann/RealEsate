from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices,intention
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from listings.models import Listing
from realtors.models import Realtor
from .forms import ContactUsForm,ApplicantForm

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    realtors = Realtor.objects.order_by('hire_date')[:3]

    context = {
        'listings': listings,
        'intention':intention,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'realtors':realtors
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)

def contactus(request):
    form=ContactUsForm()
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.info(request, 'We will contact you ASAP!')
            return redirect('index')
        else:
            messages.error(request,'Please Fill all the fields correctly!')
            return redirect('contactus')
    else:
        context={'form':form}
        messages.info(request, '  * signifies required fields!')
        return render(request, 'pages/contactus.html',context)

def privacy(request):
    return render(request, 'pages/privacy.html')

def career(request):
    form=ApplicantForm()
    if request.method=='POST':
        form=ApplicantForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'We will contact you ASAP!')
            return redirect('index')
        else:
            messages.error(request, 'PLease fill all the fields')
            return redirect('career')
    else:
        context={'form':form}
        messages.info(request,"  * signifies required fields")
        return render(request, 'pages/career.html',context)



def tandc(request):
    return render(request, 'pages/tandc.html')
