from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Customer
from .forms import CustomerForm
from django.db.models import Q

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form': form})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_form.html', {'form': form})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers/confirm_delete.html', {'customer': customer})

def customer_list(request):
    query = request.GET.get('query', '')
    salesperson = request.GET.get('salesperson', '')
    status = request.GET.get('status', '')

    customers = Customer.objects.all()

    if query:
        customers = customers.filter(
            Q(name__icontains=query) |
            Q(arabic_name__icontains=query) |
            Q(tax_registration_number__icontains=query) |
            Q(cr_number__icontains=query) |
            Q(primary_contact__icontains=query) |
            Q(mobile_number__icontains=query) |
            Q(salesperson__icontains=query)
        )

    if salesperson:
        customers = customers.filter(salesperson=salesperson)

    if status:
        customers = customers.filter(status=status)

    salespersons = customers.values_list('salesperson', flat=True).distinct()

    return render(request, 'customers/customer_list.html', {
        'customers': customers,
        'query': query,
        'salesperson': salesperson,
        'status': status,
        'salespersons': salespersons
    })
