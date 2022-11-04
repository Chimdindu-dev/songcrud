from django.urls import path
from . import views

urlpatterns = [
    path('',views.song_list,name='song-list'),
    path('create/',views.song_create,name='create-song'),
    path('edit/',views.song_edit,name='edit-song'),
    path('delete/',views.song_delete,name='delete-song'),
]