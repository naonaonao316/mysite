from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /dashboard/
    url(r'^$', views.index, name='index'),
]
