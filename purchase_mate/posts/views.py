from django.shortcuts import render

# Create your views here.
def recent_postlist(request):
    return render(request,'recent_postlist.html')

def makepost(request):
    return render(request,'makepost.html')

