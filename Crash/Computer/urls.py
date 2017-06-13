from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.computer_home, name='computer_home'),
    url(r'^transistor$', views.transistor_list, name='transistor_list'),
    url(r'^transistor/(?P<pk>[0-9]+)/$', views.transistor_update.as_view(), name='transistor_update'),
]
