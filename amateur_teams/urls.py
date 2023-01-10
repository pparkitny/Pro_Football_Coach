from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('coaches/', views.coach_list),
    path('coaches/<int:pk>/', views.coach_detail),
]
