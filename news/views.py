from django.views.generic import ListView, DetailView
from .models import News, PageSeo


class NewsAll(ListView):
    model = News
    template_name = 'news/news_all.html'
    context_object_name = 'news'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seo'] = PageSeo.objects.first()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).all()


class NewsOne(DetailView):
    model = News
    context_object_name = 'news_item'
