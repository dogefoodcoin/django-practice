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
from django.urls import path, include, reverse
from django.shortcuts import HttpResponse
from book.views import book_detail_query, book_detail_path, book_str, book_slug, book_path


def index(request):
    # print(reverse("book_str", kwargs={"book_id": 1}))
    # print(reverse("book_detail_query") + "?id=1&name=war")
    print(reverse("movie:movie_list"))
    return HttpResponse("Hello world")

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('book', book_detail_query, name='book_detail_query'),
    # 不加int类型说明，默认是字符串
    path('book/<int:book_id>', book_detail_path, name='book_detail_path'),
    path('book/str/<str:book_id>', book_str, name='book_str'),
    path('book/slug/<slug:book_id>', book_slug, name="book_slug"),
    path('book/path/<path:book_id>', book_path, name='book_path'),

    path('movie/', include("movie.urls"))
]
