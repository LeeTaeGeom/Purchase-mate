from django.shortcuts import render
from posts.models import Post

def showmain(request):
    if Post.objects.count() > 3:
        posts = Post.objects.all().order_by('-pk')[:4]
    else:
        posts = Post.objects.all().order_by('-pk')
    
    user = request.user
    my_posts = Post.objects.filter(writer=user)
    if my_posts.count() > 3:
        my_posts = my_posts.order_by('-pk')[:4]
    return render(request, 'main.html', {'posts':posts, 'my_posts':my_posts})