from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('dashboard/', include('dashboard_app.urls'), name='dashboard'),
    path('bookings/', include('bookings.urls'), name='booking_list'),
    path('payments/', include('payments.urls'), name='payment_list'),
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),
]
