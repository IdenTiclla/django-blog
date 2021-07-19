from django.urls import path
from django.urls.resolvers import URLPattern


urlpatterns = [
    path('notifications', views.index, name='index')
    
]