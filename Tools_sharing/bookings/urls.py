from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_bookings, name='my_bookings'),            # default route
    path('all/', views.booking_list, name='booking_list'),      # staff only
    path('book/<int:tool_id>/', views.book_order, name='book_order'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
