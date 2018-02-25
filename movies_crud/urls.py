from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.i18n import set_language

from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings

from . import views
from movies_crud import views as movies_crud_views

urlpatterns = i18n_patterns(
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    url("^admin/", include(admin.site.urls)),
)

urlpatterns += [
    # url('add/$', movies_crud_views.MoviesCreateView.as_view(), name='movies add'),
    # url('list/$', movies_crud_views.MoviesListView.as_view(), name='movies list'),
    url('movies/$', movies_crud_views.Movies, name='movies'),
    # url('genres/$', movies_crud_views.GenresView, name='genres'),
    # url('(?P<pk>\d+)/$', movies_crud_views.MoviesDetailView.as_view(), name='movies detail'),
    # url('(?P<pk>\d+)/update$', movies_crud_views.MoviesUpdateView.as_view(), name='movies update'),
    # url('(?P<pk>\d+)/delete$', movies_crud_views.MoviesDeleteView.as_view(), name='movies delete'),
]