from pydoc_data.topics import topics
from tkinter import CASCADE
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board, Topic, Post

def home(request):
  boards = Board.objects.all()
  return render(request, 'home.html', {'boards': boards})



