from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import CommentForm, PostForm
from .models import Category, Post


class PostListView(generic.ListView):
    # Template: blog/post_list.html; variável de contexto: post_list.
    model = Post


class PostDetailView(generic.DetailView):
    # Template: blog/post_detail.html; responde com 404 se o post não existir.
    # Comentários e categorias são lidos no template com post.comments.all
    # (mais recente primeiro) e post.categories.all.
    model = Post


class PostCreateView(generic.CreateView):
    # Template: blog/post_form.html.
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(generic.UpdateView):
    # Template: blog/post_form.html (o mesmo da criação).
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(generic.DeleteView):
    # GET mostra blog/post_confirm_delete.html; POST remove o post.
    model = Post
    success_url = reverse_lazy('blog:post_list')


def comment_create(request, pk):
    # O comentário sempre pertence ao post indicado na URL.
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'post': post})


class CategoryListView(generic.ListView):
    # Template: blog/category_list.html; variável de contexto: category_list.
    model = Category


def category_detail(request, pk):
    # Responde com 404 se a categoria não existir.
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category,
        'post_list': category.posts.all(),
    }
    # Reutiliza o template de listagem de posts da parte 1.
    return render(request, 'blog/post_list.html', context)
