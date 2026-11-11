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
