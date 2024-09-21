from django.urls import path
#from catalog.apps import NewappConfig
from catalog.views import contact, home

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]