from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    # O conteúdo é guardado como HTML e renderizado no template com o filtro safe.
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # O autor referencia o modelo de usuário do Django (settings.AUTH_USER_MODEL).
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # post.comments.all() devolve o comentário mais recente primeiro.
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.author} em "{self.post}"'
