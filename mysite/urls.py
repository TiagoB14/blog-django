from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# Com DEBUG=False (Render) o Django deixa de servir os arquivos estáticos
# sozinho; esta rota entrega o que o collectstatic reuniu (CSS do admin),
# sem depender de extensões.
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
