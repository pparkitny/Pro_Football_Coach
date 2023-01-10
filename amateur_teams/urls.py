from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('coaches/', views.CoachList.as_view()),
    path('coaches/<int:pk>/', views.CoachDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
