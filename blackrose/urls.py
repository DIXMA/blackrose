from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.web_view, name='web_view'),
]