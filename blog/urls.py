from django.urls import path
from .views import blog_page,blog_text

urlpatterns = [
    path('',blog_page),
    path('<int:blog_id>/',blog_text)


]