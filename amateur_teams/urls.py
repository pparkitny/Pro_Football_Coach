from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('coach/', views.CoachList.as_view()),
    path('coach/<int:pk>/', views.CoachDetail.as_view()),
    path('team/', views.TeamList.as_view()),
    path('team/<int:pk>/', views.TeamDetail.as_view()),
    path('player/', views.PlayerList.as_view()),
    path('player/<int:pk>/', views.PlayerDetail.as_view()),
    path('stats/', views.StatsList.as_view()),
    path('stats/<int:pk>/', views.StatsDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
