from django.shortcuts import render
from My_page.models import Gallery
def home(request):
    gallery = Gallery.objects

    return render(request,'home.html',{'gallerys':gallery})