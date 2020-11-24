from django.http import HttpResponse
from django.shortcuts import render

from .forms import RitargetForm
from .models import *



# Create your views here.


def home(request):
    customer = Customer.objects.all()
    orders = Order.objects.all()

    total_customer = customer.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders': orders, 'customer': customer,
               'total_customer': total_customer,
               'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}

    return render(request, "accounts/dashboard.html", context)
    # return HttpResponse('Home')


def product(request):
    product = Product.objects.all()
    return render(request, 'accounts/product.html', {'product': product})



def customer(request, cusid):
    customer = Customer.objects.get(id=cusid)
    print (cusid)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)


def target(request):
    targetlist = Ritarget.objects.all()
    form = RitargetForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form, 'targetlist': targetlist}

    return render(request, 'accounts/target.html', context)

