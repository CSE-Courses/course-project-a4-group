from django.urls import path
from . import views
from .views import getData
from .views import getMatchResults
from .views import watchingAds
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('stats/', views.stats, name='stats'),
    path('api/data/', getData, name='api-data'),
    path('api/data/profile/', getMatchResults, name='api-data-profile'),
    path('buy/', views.buy_view, name='buy'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('bracket/', views.bracket, name='bracket'),
    path('ads/', views.ads, name='ads'),
    path('ads/watchingAds', views.watchingAds, name='watching-ads'),
    path('myTournaments/', views.myTournaments, name='myTournaments'),
    path('joinTournaments/', views.joinTournaments, name='joinTournaments')
]

