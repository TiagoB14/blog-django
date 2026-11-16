# Mecatrônica com Tiago — blog com Django (PMR3304, Segunda Entrega de Laboratório)

Aplicação CRUD no estilo de um blog, com posts, comentários e categorias, feita apenas com o Django (sem extensões).

## Como rodar localmente

```
python -m venv venv
venv\Scripts\activate          (Windows)   |   source venv/bin/activate   (Linux/macOS)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed
python manage.py runserver
```

- Aplicação: http://127.0.0.1:8000/
- Administrador: http://127.0.0.1:8000/admin/

O comando `seed` cria três usuários (`ana`, `bruno`, `carla`), quatro categorias, três posts e cinco comentários de exemplo. Ele só age se ainda não houver posts no banco. Os mesmos dados podem ser criados à mão pelo administrador.

## Estrutura

| Caminho | Conteúdo |
| --- | --- |
| `mysite/` | Configurações do projeto (`settings.py`, `urls.py`) |
| `templates/base.html` | Template base |
| `blog/models.py` | Modelos `Post`, `Comment` e `Category` |
| `blog/views.py` | Views (classes genéricas e funções) |
| `blog/forms.py` | `PostForm` e `CommentForm` |
| `blog/urls.py` | URLs nomeadas do app (`blog:post_list`, `blog:post_detail`, ...) |
| `blog/templates/blog/` | Templates do app |
| `blog/management/commands/seed.py` | Comando de carga dos dados de exemplo |
| `build.sh` | Script de build para o Render |

## Histórico Git

As três versões das views da parte 1 estão em commits separados no `main`:

1. views funcionais, sem Django forms e sem validação;
2. views funcionais com um Django form;
3. views com as classes genéricas `ListView`, `DetailView`, `CreateView`, `UpdateView` e `DeleteView`.

Os comentários foram desenvolvidos no branch `comments` e as categorias no branch `categories`, ambos unidos ao `main` por merge.

## Deploy no Render

Criar um *Web Service* a partir do repositório do GitHub com:

- **Build Command:** `bash build.sh`
- **Start Command:** `gunicorn mysite.wsgi:application`
- **Variáveis de ambiente:** `SECRET_KEY` (valor aleatório) e, para ter acesso ao administrador, `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL` e `DJANGO_SUPERUSER_PASSWORD`.

Como o `db.sqlite3` não é versionado, o `build.sh` recria e popula o banco a cada deploy. No plano gratuito do Render o disco não é persistente: o que for criado pela aplicação publicada é perdido quando o serviço reinicia.
