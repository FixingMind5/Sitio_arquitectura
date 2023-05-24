from django.shortcuts import render

# Create your views here.
def buildings(request):
    return render(request, 'building.html')