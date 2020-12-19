import datetime

import sqlalchemy as sqlalchemy
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RitargetForm, MatchingForm
from .models import *

#SQLAlchemy
from sqlalchemy import select, func
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, or_
import urllib
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mssql+pyodbc://:@localhost:1433/azamenterprise?driver=SQL+Server+Native+Client+10.0")
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
    targetlist = Ritarget.objects.all().order_by('xrow').reverse()[:5]
    # Get All Data
    Students = Session.query(Student)
    maxqery = Session.query(func.max(Student.id))
    maxid = maxqery
    form = RitargetForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Add.')
        return HttpResponseRedirect('')
    context = {'form': form, 'targetlist': targetlist, 'Students': Students, 'maxid': maxid }
    return render(request, 'accounts/target.html', context)



def advnum(request):
    # GET Current Date
    today = datetime.date.today()

    # Format the date like (20-11-28 YY-MM-DD)
    today_string = today.strftime('PCMLRI-'+'%y%m'+'-')

    # For the very first time invoice_number is YY-MM-DD-001
    next_invoice_number = '000001'

    # Get Last Invoice Number of Current Year, Month and Day (20-11-28 YY-MM-DD)
    last_invoice = Ritarget.objects.filter(xrow__startswith=today_string).order_by('xrow').last()
    #last_invoice = '201128001'
    print (last_invoice)

    if last_invoice:
        # Cut 6 digit from the left and converted to int (201128:xxx)
        last_invoice_number = int(last_invoice.xrow[12:])
        #last_invoice_number = int(24554451)
        print (last_invoice_number)
        # Increment one with last three digit
        #next_invoice_number = last_invoice_number+1
        next_invoice_number = '{0:06d}'.format(last_invoice_number + 1)
        final = str(next_invoice_number)
    # Return custom invoice number
    #return today_string + next_invoice_number
    num1 = today_string + final

    form = MatchingForm(request.POST or None)
    context = {'num1': num1, 'form': form}
    return render(request, 'accounts/advice.html', context)






