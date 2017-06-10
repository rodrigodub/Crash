from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^exercise$', views.exercise_list, name='exercise_list'),
    url(r'^exercise/(?P<id>\d+)$', views.exercise_num, name='exercise_num'),
    url(r'^vector$', views.vector_list, name='vector_list'),
    url(r'^vector/(?P<id>\d+)$', views.vector_num, name='vector_num'),
]
