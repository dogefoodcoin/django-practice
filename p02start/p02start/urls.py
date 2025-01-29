"""
URL configuration for p02start project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse

from book.views import book_detail_query, book_detail_path


def index(request):
    return HttpResponse("Hello world")

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', index),
    path('book', book_detail_query),
    # 不加int类型说明，默认是字符串
    path('book/<int:book_id>', book_detail_path)
]
