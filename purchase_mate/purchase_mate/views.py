from django.shortcuts import render
from posts.models import Post

def showmain(request):
    posts = Post.objects.all().order_by('-pk')[:4]
    user = request.user
    my_posts = Post.objects.filter(writer=user).order_by('-pk')[:4]
    return render(request, 'main.html', {'posts':posts, 'my_posts':my_posts})