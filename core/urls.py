from django.urls import path

from .views import PortfolioView, ParkingView

urlpatterns = [
    path('', PortfolioView.as_view(), name='index'),
    path('parking/', ParkingView.as_view(), name='parking'),
]