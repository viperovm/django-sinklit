from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portfolio, PageSeo, PortfolioImage, PortfolioPage


def portfolio_page(request):
    page = PortfolioPage.objects.first()
    seo = PageSeo.objects.first()
    portfolio = Portfolio.objects.all()

    context = {
        'page': page,
        'seo': seo,
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/portfolio_all.html', context)


def portfolio_case(request, slug):
    case = Portfolio.objects.filter(slug=slug).first()
    img = PortfolioImage.objects.filter(portfolio__slug=slug).all()

    context = {
        'case': case,
        'img': img,
    }

    return render(request, 'portfolio/portfolio_detail.html', context)
