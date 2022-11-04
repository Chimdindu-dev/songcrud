from django.shortcuts import render, redirect
from .models import Song

# Create your views here.
def song_list(request):
    song = Song.objects.all()
    context = {
        'song' : song,
    }
    return render(request,'musicapp/list.html',context)

def song_create(request):
    return render(request,'musicapp/create.html')

def song_edit(request,pk):
    return render(request,'musicapp/edit.html')

def song_delete(request,pk):
    return render(request,'musicapp/delete.html')

