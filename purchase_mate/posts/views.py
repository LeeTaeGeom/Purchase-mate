from django.shortcuts import redirect, render, get_object_or_404
from .models import Post

# Create your views here.

def recent_postlist(request):
    post = Post.objects.all()
    return render(request,'recent_postlist.html',{'post':post})

def makepost(request):
    return render(request, 'makepost.html')

def detail(request,id):
    post = get_object_or_404(Post, pk=id)
    return render(request,'detail.html',{'post':post})

def create(request):
    makepost_post = Post()
    makepost_post.title = request.POST['title']
    makepost_post.writer=request.user
    makepost_post.quantity=request.POST['quantity']
    makepost_post.price=request.POST['price']
    makepost_post.people=request.POST['people']
    makepost_post.save()
    return redirect('posts:detail',makepost_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'edit.html',{'post':edit_post})

def update(request, id):
    update_post= Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer=request.user
    update_post.quantity=request.POST['quantity']
    update_post.price=request.POST['price']
    update_post.people=request.POST['people']
    update_post.save()
    return redirect('posts:detail',update_post.id)

def delete(request,id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect("posts:recent_postlist")
