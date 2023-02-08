from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

from .models import Index_bgs
# Create your views here.

#def index(request):
#    return render(request,'index.html')


blood_groups ={
    'op':'O+',
    'on':'O-',
    'ap':'A+',
    'an':'A-',
    'bp':'B+',
    'bn':'B-',
    'abp':'AB+',
    'abn':'AB-'
}

def about(request):
    return render(request,'about-me.html' )

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    dict_form={
        'form': form
    }
    return render(request,'contact-us.html', dict_form )

def index(request):
    dict_search = {
        'di_search' : Index_bgs.objects.all()
    }
    return render(request,'index.html',dict_search)

