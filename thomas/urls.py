from django.conf.urls import url
from thomas.views import IndexView

urlpatterns = [
    url('^.*$', IndexView.as_view(), name='index'),
]