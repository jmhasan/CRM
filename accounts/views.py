import sqlalchemy as sqlalchemy
from django.http import HttpResponse
from django.shortcuts import render

from .forms import RitargetForm
from .models import *

#SQLAlchemy
from sqlalchemy import select, func
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, or_
import urllib
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("mssql+pyodbc://:@localhost:1433/VAT?driver=SQL+Server+Native+Client+10.0")
conn = engine.connect()
Session = sessionmaker(bind=engine)
Session = Session()
Base =declarative_base()
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

    # Get All Data
    Students = Session.query(Student)
    maxqery = Session.query(func.max(Student.id))
    for i in maxqery:
        print(i)

    maxid = "PCML-"+i[0]+1
    print(maxid)

    #print(maxqery.name)
    form = RitargetForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form, 'targetlist': targetlist, 'Students':Students, 'maxid': maxqery }
    return render(request, 'accounts/target.html', context)



