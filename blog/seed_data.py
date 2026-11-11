"""Dados de exemplo usados pelo comando `python manage.py seed`.

Atendem ao mínimo pedido na parte 4 do enunciado:
- 3 posts, sendo 1 sem comentários e 2 com múltiplas categorias;
- cada post comentado tem de 2 a 3 comentários;
- 3 categorias, com cada post em ao menos uma delas.
"""

USERS = [
    {'username': 'ana', 'first_name': 'Ana'},
    {'username': 'bruno', 'first_name': 'Bruno'},
    {'username': 'carla', 'first_name': 'Carla'},
]

CATEGORIES = [
    {
        'name': 'Django',
        'description': 'Posts sobre o framework Django: modelos, views, templates e deploy.',
    },
    {
        'name': 'Front-end',
        'description': 'HTML, CSS e organização de templates.',
    },
    {
        'name': 'Banco de Dados',
        'description': 'Modelagem de dados, SQLite e consultas SQL.',
    },
]

POSTS = [
    {
        'title': 'Do Hugo ao Django: de site estático a blog dinâmico',
        'pub_date': '2026-10-20T10:00:00-03:00',
        'categories': ['Django', 'Front-end'],
        'content': (
            '<p>Na primeira entrega de laboratório o site foi feito com o '
            '<strong>Hugo</strong>, um gerador de sites estáticos: cada página '
            'nasce de um arquivo Markdown e o HTML final é gerado antes da '
            'publicação.</p>\n'
            '<p>Com o <strong>Django</strong> a lógica muda. O conteúdo fica em '
            'um banco de dados e o HTML é montado a cada requisição, o que '
            'permite criar, editar e remover posts pela própria aplicação.</p>\n'
            '<h2>O que mudou na prática</h2>\n'
            '<ul>\n'
            '<li>os arquivos de conteúdo viraram registros do modelo <code>Post</code>;</li>\n'
            '<li>os leiautes do Hugo viraram templates que estendem um <code>base.html</code>;</li>\n'
            '<li>o site passou a aceitar comentários, algo impossível em um site puramente estático.</li>\n'
            '</ul>\n'
            '<p>A estrutura em HTML5 (<code>header</code>, <code>nav</code>, '
            '<code>main</code> e <code>footer</code>) e as ideias de CSS da '
            'primeira entrega continuam valendo.</p>'
        ),
        'comments': [
            {
                'author': 'ana',
                'pub_date': '2026-10-20T14:12:00-03:00',
                'text': 'Boa comparação! Também achei o Hugo ótimo para portfólio, mas sem banco de dados ele fica limitado.',
            },
            {
                'author': 'bruno',
                'pub_date': '2026-10-21T09:40:00-03:00',
                'text': 'Dá para reaproveitar o CSS inteiro da primeira entrega ou precisou mudar muita coisa?',
            },
            {
                'author': 'carla',
                'pub_date': '2026-10-22T19:05:00-03:00',
                'text': 'A herança de templates do Django lembra bastante o baseof.html do Hugo.',
            },
        ],
    },
    {
        'title': 'Modelos, migrações e o arquivo db.sqlite3',
        'pub_date': '2026-10-28T15:30:00-03:00',
        'categories': ['Django', 'Banco de Dados'],
        'content': (
            '<p>No Django cada modelo é uma classe Python que vira uma tabela no '
            'banco de dados. O blog tem três modelos: <code>Post</code>, '
            '<code>Comment</code> e <code>Category</code>.</p>\n'
            '<h2>Do modelo à tabela</h2>\n'
            '<ol>\n'
            '<li><code>python manage.py makemigrations</code> gera o arquivo de migração a partir dos modelos;</li>\n'
            '<li><code>python manage.py migrate</code> aplica a migração e cria as tabelas no <code>db.sqlite3</code>.</li>\n'
            '</ol>\n'
            '<p>As tabelas recebem o nome do app seguido do nome do modelo: '
            '<code>blog_post</code>, <code>blog_comment</code> e '
            '<code>blog_category</code>. A relação muitos-para-muitos entre posts '
            'e categorias ganha uma tabela própria, a '
            '<code>blog_post_categories</code>.</p>\n'
            '<p>Como o banco é um único arquivo, dá para abri-lo no DB Browser '
            'for SQLite e consultar os dados diretamente com SQL.</p>'
        ),
        'comments': [
            {
                'author': 'bruno',
                'pub_date': '2026-10-28T18:20:00-03:00',
                'text': 'Não sabia que a relação muitos-para-muitos criava uma tabela separada. Faz sentido!',
            },
            {
                'author': 'ana',
                'pub_date': '2026-10-29T08:55:00-03:00',
                'text': 'O DB Browser ajuda muito a entender o que o ORM está fazendo por baixo dos panos.',
            },
        ],
    },
    {
        'title': 'Flexbox ou Grid? Notas de CSS para o template base',
        'pub_date': '2026-11-05T09:15:00-03:00',
        'categories': ['Front-end'],
        'content': (
            '<p>O template base do blog usa <strong>Flexbox</strong> no cabeçalho: '
            'o título fica à esquerda e os links de navegação à direita, com '
            '<code>justify-content: space-between</code>.</p>\n'
            '<p>Uma regra prática que tem funcionado:</p>\n'
            '<ul>\n'
            '<li><strong>Flexbox</strong> para alinhar itens em uma única direção (uma linha ou uma coluna);</li>\n'
            '<li><strong>Grid</strong> quando o leiaute tem linhas e colunas ao mesmo tempo.</li>\n'
            '</ul>\n'
            '<p>Para telas estreitas, uma <em>media query</em> remove as margens '
            'do conteúdo principal e o <code>flex-wrap</code> deixa a navegação '
            'quebrar de linha.</p>'
        ),
        'comments': [],
    },
]
