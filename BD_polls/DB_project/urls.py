from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
import questions_and_ratings.urls

admin.autodiscover()

urlpatterns = i18n_patterns('',
                            url(r'^admin/', include(admin.site.urls)),  # NOQA
                            url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
                                {'sitemaps': {'cmspages': CMSSitemap}}),
                            url(r'^questions_and_ratings/', include(questions_and_ratings.urls)),
                            url(r'^', include('social.apps.django_app.urls', namespace='social')),
                            url(r'^login/$', 'views.login'),
                            url(r'^logout/$', 'views.logout'),
                            url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
