from django.conf.urls import url
from clientes.views import cliente_nuevo

urlpatterns = [
    url(r'^nuevo/$', cliente_nuevo, name='cliente_nuevo'),
]
