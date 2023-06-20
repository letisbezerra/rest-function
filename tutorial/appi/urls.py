from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from appi import views

urlpatterns = [
    path('appi/', views.AppiList.as_view()),
    path('appi/<int:pk>/', views.AppiDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)