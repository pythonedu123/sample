from django.shortcuts import render, redirect
from django.http import HttpResponse
from  . models import movie
from  .forms import movieforms
# Create your views here.
# def demo(request):
#     return HttpResponse("hello world")
# def app(request):
#     return render(request,"index.html")
def index(request):
    Movie=movie.objects.all()
    context={
        'movie_list':Movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    Movie=movie.objects.get(id=movie_id)

    return render(request,'details.html',{'Movie':Movie})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        Movie1=movie(name=name,desc=desc,year=year,img=img)
        Movie1.save()

    return render(request,'add.html')

def update(request,id):
    mov=movie.objects.get(id=id)
    form=movieforms(request.POST or None, request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')
