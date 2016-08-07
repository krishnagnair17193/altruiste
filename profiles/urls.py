from django.conf.urls import url


from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^register/', TemplateView.as_view(template_name='accounts/register.html'), name='register'),
    url(r'^logout/', logout, {'next_page': '/login/'}, name='logout'),
]
