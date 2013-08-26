from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('home.views',
        # /
        url(r'^download', 'downloadFile'),
        url(r'^datacart', 'make_datasetId_form'),
        url(r'^workbench', 'run_main_window'),
        url(r'^calculate', 'calculate'),
        url(r'^plot/boxfill', 'make_boxfill'),
        url(r'^main/(?P<json_param>)\w*$', 'make_main_window'),
        url(r'^plot/$', 'make_main_window'),
        url(r'^/?$', 'show_index'),
        url(r'^logout/$', 'logout_view'),
        url(r'^boxfill/$', 'boxfill'),
        )

