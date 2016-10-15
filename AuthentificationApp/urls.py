from django.conf.urls import url, include
from django.views.generic import CreateView

from AuthentificationApp.forms import UserCreationFormEnriched

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url('^register/$', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationFormEnriched
    )),
]
