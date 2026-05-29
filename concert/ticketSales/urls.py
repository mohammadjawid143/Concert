from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ticketSales/location/list/', views.locationa_list_view, name='location_list'),
    path('ticketSales/details/<int:concert_id>/',
         views.concertDetails, name='details'),  # Corrected spelling
    path('ticketSales/details/<int:time_id>/', views.time_details,
         name='time_details'),  # Corrected spelling
    path('ticketSales/time/list/', views.time_view, name='time'),
    path('ticketSales/ConcertEdit/<int:concert_id>/', views.concertedite, name='Edit'),
]
