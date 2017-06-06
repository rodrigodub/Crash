from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^vector$', views.vector_list, name='vector_list'),
    url(r'^vector/(?P<id>\d+)$', views.vector_num, name='vector_num'),
]
