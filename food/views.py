from django.shortcuts import render

def home(request):
    return render(request, 'food/home.html')

# Create your views here.
