"""Gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
# import blog.views
#导入static方法和settings模块用来导入media的网址和根目录
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('blog/',include('blog.urls'))#django推荐的格式
    # path('blog',blog.views.blog_page)
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)#在setting.py文件中设置好media的网址和根目录后在此处按照规定格式添加
