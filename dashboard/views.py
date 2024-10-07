from django.shortcuts import render
from properties.models import Property
from rentals.models import Rental
from payments.models import Payment
# Create your views here.

def dashboard(request):
  properties = Property.objects.all()
  rentals = Rental.objects.all()
  payments = Payment.objects.all()
  return render(request, 'dashboard/dashboard.html', {'properties': properties, 'rentals': rentals, 'payments': payments})