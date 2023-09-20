from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Booking, Menu

class BookingModelTest(TestCase):

    def test_booking_invalid_guests(self):
        # Create a Booking instance with invalid no_of_guests value
        booking = Booking(name="Test Booking", no_of_guests=0)
        # Use assertRaises to check if a ValidationError is raised
        with self.assertRaises(ValidationError):
            booking.full_clean()

class MenuModelTest(TestCase):

    def test_menu_invalid_inventory(self):
        # Create a Menu instance with invalid inventory value
        menu = Menu(title="Test Menu", price=10.99, inventory=10)  # Invalid inventory value
        # Use assertRaises to check if a ValidationError is raised
        with self.assertRaises(ValidationError):
            menu.full_clean()
