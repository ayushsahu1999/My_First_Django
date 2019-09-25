from django.conf.urls import include
from AppTwo import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
