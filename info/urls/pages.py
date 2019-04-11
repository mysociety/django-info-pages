from django.conf.urls import url

from ..views import InfoPageView


urlpatterns = [
    url(r'^$',                  InfoPageView.as_view(), { 'slug': 'index' } ),
    url(r'^(?P<slug>[\w\-]+)$', InfoPageView.as_view(), name='info_page' ),
]
