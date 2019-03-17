from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^mudar-dados/$', views.update_user, name="update_user"),
    url(r'^mudar-senha/$', views.update_password, name="update_password"),
]
