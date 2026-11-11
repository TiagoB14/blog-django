# Versão 2: views funcionais utilizando um Django form (PostForm).
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list': post_list})


def post_detail(request, pk):
    # Responde com 404 se o post não existir.
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')
    # GET: mostra a página de confirmação.
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
