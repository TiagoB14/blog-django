# Versão 3: views com as classes genéricas do Django.
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import PostForm
from .models import Post


class PostListView(generic.ListView):
    # Template: blog/post_list.html; variável de contexto: post_list.
    model = Post


class PostDetailView(generic.DetailView):
    # Template: blog/post_detail.html; responde com 404 se o post não existir.
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
