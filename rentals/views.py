from django.shortcuts import render, redirect, get_object_or_404
from .models import Rental
from .forms import RentalForm
# Create your views here.
def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'rentals/rental_list.html', {'rentals': rentals})

def rental_detail(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    return render(request, 'rentals/rental_detail.html', {'rental': rental})

def rental_create(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental_list')
    else:
        form = RentalForm()
    return render(request, 'rentals/rental_form.html', {'form': form})

def rental_update(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    if request.method == 'POST':
        form = RentalForm(request.POST, instance=rental)
        if form.is_valid():
            form.save()
            return redirect('rental_list')
    else:
        form = RentalForm(instance=rental)
    return render(request, 'rentals/rental_form.html', {'form': form})

def rental_delete(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    if request.method == 'POST':
        rental.delete()
        return redirect('rental_list')
    return render(request, 'rentals/rental_confirm_delete.html', {'rental': rental})