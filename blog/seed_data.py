"""Dados de exemplo usados pelo comando `python manage.py seed`.

Os posts reaproveitam o conteúdo dos projetos do portfólio da primeira
entrega. O conjunto atende ao mínimo pedido na parte 4 do enunciado:
- 3 posts, sendo 1 sem comentários e 2 com múltiplas categorias;
- cada post comentado tem de 2 a 3 comentários;
- 4 categorias, com cada post em ao menos uma delas.
"""

USERS = [
    {'username': 'ana', 'first_name': 'Ana'},
    {'username': 'bruno', 'first_name': 'Bruno'},
    {'username': 'carla', 'first_name': 'Carla'},
]

CATEGORIES = [
    {
        'name': 'Modelagem de Sistemas',
        'description': 'Modelos para descrever e analisar o funcionamento de sistemas.',
    },
    {
        'name': 'Automação',
        'description': 'Controle e automação de sistemas a eventos discretos.',
    },
    {
        'name': 'Desenvolvimento Web',
        'description': 'Aplicações, interfaces e plataformas web.',
    },
    {
        'name': 'Eletrônica',
        'description': 'Circuitos analógicos e experiências de laboratório.',
    },
]

POSTS = [
    {
        'title': 'USP SOS',
        'pub_date': '2026-09-16T10:00:00-03:00',
        'categories': ['Modelagem de Sistemas', 'Desenvolvimento Web'],
        'content': (
            '<p>Plataforma web para mapear e reportar problemas de '
            'infraestrutura no campus, como lâmpadas queimadas, buracos e '
            'vazamentos.</p>\n'
            '<h2>O que foi feito</h2>\n'
            '<ul>\n'
            '<li>Levantamento de requisitos junto aos usuários</li>\n'
            '<li>Modelagem do sistema de informação</li>\n'
            '<li>Protótipo da interface de reporte de ocorrências</li>\n'
            '</ul>\n'
            '<h2>Tecnologias</h2>\n'
            '<p>HTML, CSS, JavaScript e banco de dados.</p>'
        ),
        'comments': [
            {
                'author': 'ana',
                'pub_date': '2026-09-16T14:12:00-03:00',
                'text': 'Muito útil! Perto do meu prédio tem uma lâmpada queimada há semanas e eu nunca soube onde avisar.',
            },
            {
                'author': 'bruno',
                'pub_date': '2026-09-17T09:40:00-03:00',
                'text': 'O protótipo já permite enviar uma foto junto com a ocorrência?',
            },
            {
                'author': 'carla',
                'pub_date': '2026-09-18T19:05:00-03:00',
                'text': 'Seria legal ver as ocorrências em um mapa do campus.',
            },
        ],
    },
    {
        'title': 'Monografia: Redes de Petri',
        'pub_date': '2026-09-24T15:30:00-03:00',
        'categories': ['Automação', 'Modelagem de Sistemas'],
        'content': (
            '<p>Modelagem e controle de um sistema de automação usando Redes de '
            'Petri, na disciplina de Sistemas a Eventos Discretos.</p>\n'
            '<h2>Etapas</h2>\n'
            '<ul>\n'
            '<li>Descrição do sistema e de seus estados</li>\n'
            '<li>Modelagem em Rede de Petri</li>\n'
            '<li>Análise de propriedades como vivacidade e limitação</li>\n'
            '</ul>\n'
            '<h2>Resultado</h2>\n'
            '<p>Um modelo que representa o funcionamento do sistema e permite '
            'verificar sua segurança.</p>'
        ),
        'comments': [
            {
                'author': 'bruno',
                'pub_date': '2026-09-24T18:20:00-03:00',
                'text': 'Qual ferramenta você usou para desenhar e simular a rede?',
            },
            {
                'author': 'ana',
                'pub_date': '2026-09-25T08:55:00-03:00',
                'text': 'Verificar a vivacidade antes de implementar o controle evita muito retrabalho.',
            },
        ],
    },
    {
        'title': 'Amplificadores Operacionais',
        'pub_date': '2026-09-29T09:15:00-03:00',
        'categories': ['Eletrônica'],
        'content': (
            '<p>Estudo experimental de circuitos com amplificadores '
            'operacionais em laboratório.</p>\n'
            '<h2>Circuitos estudados</h2>\n'
            '<ul>\n'
            '<li>Amplificador inversor</li>\n'
            '<li>Amplificador somador</li>\n'
            '<li>Filtro passa-baixas ativo</li>\n'
            '</ul>\n'
            '<h2>Aprendizados</h2>\n'
            '<p>Análise do ganho, da resposta em frequência e das diferenças '
            'entre o comportamento teórico e o medido.</p>'
        ),
        'comments': [],
    },
]
