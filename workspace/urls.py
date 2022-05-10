from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('spaces/', views.SpaceList.as_view()),
    path('spaces/<slug:slug>', views.SpaceDetail.as_view()),
    path('plans/', views.PlanList.as_view()),
    path('plans/<slug:slug>', views.PlanDetail.as_view()),
    path('bookings/', views.BookingList.as_view()),
    path('bookings/<slug:slug>', views.BookingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)