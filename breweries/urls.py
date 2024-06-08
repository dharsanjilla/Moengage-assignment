# breweries/urls.py
# breweries/urls.py

from django.urls import path
from .views import signup, search_breweries
from . import views 

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('search_breweries/', views.search_breweries, name='search_breweries'),
    
    path('brewery/<uuid:brewery_id>/add_review/', views.add_review, name='add_review'),
    path('brewery/<uuid:brewery_id>/', views.brewery_detail, name='brewery_detail'),
]



    





