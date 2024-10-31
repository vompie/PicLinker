from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import markdown
import os


def home_page(request: HttpRequest) -> HttpResponse:
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    readme_html = markdown.markdown(readme_content)
    return render(request, 'home.html', {'readme_html': readme_html})
