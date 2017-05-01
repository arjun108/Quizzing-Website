from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_id>[0-9]+)/$', views.category, name = 'category'),
    url(r'^(?P<category_id>[0-9]+)/vote/$', views.vote, name= 'vote'),
    url(r'^result/(?P<score>[0-9]+)/$', views.result, name= 'result'),
]