from django.views.generic import ListView
from .models import Reviews, PageSeo


class ReviewsAll(ListView):
    model = Reviews
    template_name = 'reviews/reviews_all.html'
    context_object_name = 'reviews'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отзывы'
        context['seo'] = PageSeo.objects.first()
        return context

    def get_queryset(self):
        return Reviews.objects.all()
