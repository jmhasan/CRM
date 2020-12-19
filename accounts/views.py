import datetime
import sqlalchemy as sqlalchemy
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics
from django.core.paginator import Paginator
from .forms import RitargetForm, MatchingForm
from .models import *

# SQLAlchemy
from sqlalchemy import select, func
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, or_
import urllib
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .serializers import MatchingSerializer, MatchingSerializerNew

engine = create_engine("mssql+pyodbc://:@localhost:1433/VAT?driver=SQL+Server+Native+Client+10.0")
conn = engine.connect()
Session = sessionmaker(bind=engine)
Session = Session()
Base = declarative_base()


# Create your views here.


def home(request):
    customer = Customer.objects.all()
    orders = Order.objects.all()

    total_customer = customer.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

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
    print(cusid)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)


def target(request):
    targetlist = Ritarget.objects.all().order_by('xrow').reverse()[:5]

    #pagination funciton for RI target list
    """contact_list = Ritarget.objects.all()
    paginator = Ritarget(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)"""

    # Get All Data
    Students = Session.query(Student)
    maxqery = Session.query(func.max(Student.id))
    maxid = maxqery
    form = RitargetForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form, 'targetlist': targetlist, 'Students': Students, 'maxid': maxid}
    return render(request, 'accounts/target.html', context)


def advnum(request):
    form = MatchingForm(request.POST or None)
    context = {'form': form}
    return render(request, 'accounts/advice.html', context)


class APIOutletPaymentMgmtNew(generics.CreateAPIView):
    queryset = Session.query(Student)
    # queryset = Student.objects.all()
    serializer_class = MatchingSerializer



class MatchingSerializerView(generics.CreateAPIView):
    queryset = Session.query(Matching)
    # queryset = Student.objects.all()
    serializer_class = MatchingSerializerNew


