from django.shortcuts import render
from .models import Payment
# Create your views here.
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payments/payment_list.html', {'payments': payments})