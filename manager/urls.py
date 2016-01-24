from django.conf.urls import url

from . import views

urlpatterns = [
    #ex: /manager/
    url(r'^$', views.index, name='index'),
    #ex: /manager/5/
    url(r'^(?P<questionID>[0-9]+)/$', views.detail, name='index'),
    #ex: /manager/5/results/
    url(r'^(?P<questionID>[0-9]+)/results/$', views.results, name='results'),
    #ex: /manager/5/vote/
    url(r'^(?P<questionID>[0-9]+)/vote/$', views.vote, name='vote'),
]