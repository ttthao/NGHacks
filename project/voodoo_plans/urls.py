from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit$', views.itnrsub, name='submit'),
    url(r'^results$', views.algo_results, name='results')
]
