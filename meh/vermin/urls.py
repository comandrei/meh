from django.conf.urls import patterns,  url

from .views import Index

urlpatterns = patterns(
    '',
    url('^$', Index.as_view())
)
