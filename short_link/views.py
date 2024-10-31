from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .forms import UrlForm
from .models import Url


def create_url(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('url_list')
    else:
        form = UrlForm()
    return render(request, 'create_url.html', {'form': form})


def url_list(request: HttpRequest) -> HttpResponse:
    urls = Url.objects.all()
    return render(request, 'url_list.html', {'urls': urls})


def redirect_url(request: HttpRequest, short_url: str) -> HttpResponse:
    url = get_object_or_404(Url, short_url=short_url)
    return redirect(url.url)
