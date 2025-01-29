from django.shortcuts import HttpResponse

# Create your views here.

def movie_list(request):
    return HttpResponse("Movie List")


def movie_detail(request, movie_id):
    return HttpResponse(f"id: {movie_id}")