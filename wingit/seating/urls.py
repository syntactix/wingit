from django.conf.urls import url
from seating.views import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]