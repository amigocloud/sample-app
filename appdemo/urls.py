from django.conf import settings
from django.conf.urls import patterns, url

from .views import IndexView


urlpatterns = patterns(
    '',
    url(r'^/?$', IndexView.as_view(), name='index'),
    # Static files
    url(r'^static/(.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
)
