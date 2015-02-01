from django.conf.urls import patterns, url
from .views import question_view, rating_view


urlpatterns = patterns('',
                       url(r'^question/(?P<question_id>\d+)$', question_view, name='question'),
                       url(r'^rating/(?P<rating_id>\d+)$', rating_view, name='rating'),
)