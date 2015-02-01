from django.conf.urls import patterns, url
from .views import question_view


urlpatterns = patterns('',
                       url(r'^question/(?P<question_id>\d+)$', question_view, name='question'),
)