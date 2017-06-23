from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from aloisioimoveis.core.views import home, rent, buy, search, contact, company

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^alugar/$', rent, name='rent'),
    url(r'^comprar/$', buy, name='buy'),
    url(r'^buscar/$', search, name='search'),
    url(r'^imovel/', include('aloisioimoveis.properties.urls', namespace='records')),
    url(r'^empresa/$', company, name='company'),
    url(r'^contato/$', contact, name='contact'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
