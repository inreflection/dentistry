from django.shortcuts import render, get_object_or_404
from .models import News
from django.views.generic import DetailView
def allNews(request):
    news_list = News.objects.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news/allNews.html', context)

def newsDetail(request, pk):
    news = get_object_or_404(News, pk=pk)
    context = {
        'news': news
    }
    return render(request, 'news/newsDetail.html', context)