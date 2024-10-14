from django.shortcuts import render

# Create your views here.

def index(request):
    """A view to Return the Index Page"""
    return render(request, 'home/index.html')