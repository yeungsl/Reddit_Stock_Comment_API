# api/urls.py

from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = {
    path('bucketlists/', CreateView.as_view(), name="create"),
    re_path(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)