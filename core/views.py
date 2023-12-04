from django.shortcuts import render, redirect
from .models import Post

def index(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'index.html', context)

def create(request):
    print(dir(request.headers.items))
    return render(request, 'create.html')

def salvar(request):
    titulo = request.POST.get('titulo')
    post = request.POST.get('post')
    Post.objects.create(titulo=titulo, post=post)
    return redirect(index)

def editar(request, id):
    post = Post.objects.get(id=id)

    context = {
        'posts': post
    }
    return render(request, 'update.html', context)

def update(request, id):
    titulo = request.POST.get('titulo')
    post = request.POST.get('post')
    posts = Post.objects.get(id=id)

    posts.titulo = titulo
    posts.post = post
    posts.save()

    return redirect(index)

def deletar(request, id):
    posts = Post.objects.get(id=id)
    posts.delete()
    return redirect(index)