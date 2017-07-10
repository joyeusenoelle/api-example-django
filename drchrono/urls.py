from django.conf.urls import include, url
from django.views.generic import TemplateView

from views import get_users


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^accounts/profile/', get_users)
]

# url(r'^complete/drchrono/', TemplateView.as_view(template_name='auth.html'), name='auth'),
