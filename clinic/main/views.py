from django.shortcuts import render
from service.models import ServiceCategory, Service


def home(request):
    categories = ServiceCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


def price(request):
    categories = ServiceCategory.objects.all()
    services = Service.objects.all()
    context = {
        'categories': categories,
        'services': services
    }
    return render(request, 'main/price.html', context)


