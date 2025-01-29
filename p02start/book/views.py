from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def book_detail_query(request):
    book_id = request.GET.get('id')
    name = request.GET.get('name')
    return HttpResponse(f"id: {book_id}, name: {name}")

def book_detail_path(request, book_id):
    return HttpResponse(f"id: {book_id}")