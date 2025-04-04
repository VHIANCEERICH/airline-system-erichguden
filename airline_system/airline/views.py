from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight, Booking, Passenger

# 6.1 List Available Flights
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'airline/flight_list.html', {'flights': flights})

# 6.2 Add a Flight Booking
def book_flight(request, flight_id):
    passenger = Passenger.objects.get(id=1)  # Temporary: Replace with logged-in user logic
    flight = get_object_or_404(Flight, id=flight_id)
    Booking.objects.create(passenger=passenger, flight=flight, seat_number="A1", status="Confirmed")
    return redirect('flight_list')
