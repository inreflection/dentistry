from django.shortcuts import render
from .models import ServiceCategory, Service
from django.shortcuts import render, get_object_or_404

def categoryService(request):
    categories = ServiceCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'service/service.html', context)

def category_detail(request, pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    services = Service.objects.filter(category=category)
    context = {
        'category': category,
        'services': services
    }
    return render(request, 'service/category_detail.html', context)
