from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Image
from .forms import ImageUploadForm


def upload_image(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
        return redirect('view_image', image.id)
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})


def list_images(request):
    images = Image.objects.all()
    return render(request, 'list_images.html', {'images': images})


def view_image(request: HttpRequest, image_id: int) -> HttpResponse:
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'view_image.html', {'image': image})


def api_upload_image(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            return JsonResponse({'id': image.id, 'url': image.image.url}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)
