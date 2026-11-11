from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from blog.models import Category, Comment, Post
from blog.seed_data import CATEGORIES, POSTS, USERS


class Command(BaseCommand):
    help = 'Popula o banco com usuários, categorias, posts e comentários de exemplo.'

    @transaction.atomic
    def handle(self, *args, **options):
        if Post.objects.exists():
            self.stdout.write('O banco já possui posts; nada foi alterado.')
            return

        User = get_user_model()
        users = {}
        for data in USERS:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={'first_name': data['first_name']},
            )
            if created:
                # Usuários de exemplo servem só como autores; não fazem login.
                user.set_unusable_password()
                user.save()
            users[data['username']] = user

        categories = {}
        for data in CATEGORIES:
            category, _ = Category.objects.get_or_create(
                name=data['name'],
                defaults={'description': data['description']},
            )
            categories[data['name']] = category

        for data in POSTS:
            post = Post.objects.create(
                title=data['title'],
                content=data['content'],
                pub_date=datetime.fromisoformat(data['pub_date']),
            )
            post.categories.set([categories[name] for name in data['categories']])
            for comment in data['comments']:
                Comment.objects.create(
                    post=post,
                    author=users[comment['author']],
                    text=comment['text'],
                    pub_date=datetime.fromisoformat(comment['pub_date']),
                )

        self.stdout.write(self.style.SUCCESS(
            f'Banco populado: {Post.objects.count()} posts, '
            f'{Category.objects.count()} categorias e '
            f'{Comment.objects.count()} comentários.'
        ))
