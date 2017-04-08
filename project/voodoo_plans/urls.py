from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^complete/', views.complete, name='complete'),
    url(r'^submit$', views.itnrsub, name='submit'),
    url(r'^results$', views.algo_results, name='results'),
    url(r'^itinerary$', views.displ_itin, name='itinerary')
]
