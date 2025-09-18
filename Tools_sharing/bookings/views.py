from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from dashboard_app.models import Tool   # ✅ adjust if Tool is in another app


@login_required(login_url="/accounts/login/")
def book_order(request, tool_id):
    """Book a tool if user is logged in"""
    tool = get_object_or_404(Tool, id=tool_id)

    if request.method == "POST":
        # Create booking for logged-in user
        Booking.objects.create(
            user=request.user,
            tool=tool,
            status="Booked"   # ✅ Booking model must have this field
        )
        messages.success(request, f"Your booking for {tool.name} is confirmed!")
        return redirect("my_bookings")

    return render(request, "bookings/confirm_booking.html", {"tool": tool})


@login_required(login_url="/accounts/login/")
def my_bookings(request):
    """Show all bookings of the logged-in user"""
    bookings = Booking.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})


@login_required(login_url="/accounts/login/")
def cancel_booking(request, booking_id):
    """Allow user to cancel a booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.status != "Cancelled":
        booking.status = "Cancelled"
        booking.save()
        messages.info(request, f"Your booking for {booking.tool.name} has been cancelled.")

    return redirect("my_bookings")


@login_required(login_url="/accounts/login/")
def booking_list(request):
    """Show all bookings (staff only)"""
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to view all bookings.")
        return redirect("my_bookings")

    bookings = Booking.objects.all().order_by("-created_at")
    return render(request, "bookings/booking_list.html", {"bookings": bookings})
