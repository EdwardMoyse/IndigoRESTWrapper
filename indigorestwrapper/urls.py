from django.conf.urls import url
from indigorestwrapper import views

urlpatterns = [
    url(r'^devices/$', views.device_list),
    url(r'^basic_devices/$', views.basic_device_list),
    url(r'^device/(?P<id>[0-9]+)/$', views.device),
    url(r'^device_history/(?P<id>[0-9]+)/$', views.device_history),
]