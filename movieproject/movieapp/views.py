from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movieform
# Create your views here.
from .models import Movie


def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }

    return render(request, 'movies.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dec = request.POST.get('dec')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, dec=dec, year=year, img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')


def SearchResultsView(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        results = Movie.objects.all().filter(Q(name__icontains=searched) | Q(dec__icontains=searched))
        return render(request, 'search.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'search.html')