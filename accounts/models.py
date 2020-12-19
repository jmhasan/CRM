import datetime

from django.db import models

# SQLAlchemy
from sqlalchemy.orm import *
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, or_
import urllib
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mssql+pyodbc://:@localhost:1433/azamenterprise?driver=SQL+Server+Native+Client+10.0")
conn = engine.connect()
Session = sessionmaker(bind=engine)
Session = Session()
Base = declarative_base()


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATAGORY = (
        ('Indoor', 'Indor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATAGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

def advnum():
    # GET Current Date
    today = datetime.date.today()
    # Format the date like (20-11-28 YY-MM-DD)
    today_string = today.strftime('PCMLRI-'+'%y%m'+'-')

    # Get Last Invoice Number of Current Year, Month and Day (20-11-28 YY-MM-DD)
    last_invoice = Ritarget.objects.filter(xrow__startswith=today_string).order_by('xrow').last()
    if last_invoice:
        # Cut 6 digit from the left and converted to int (201128:xxx)
        last_invoice_number = int(last_invoice.xrow[12:])
        #last_invoice_number = int(24554451)
        print (last_invoice_number)
        # Increment one with last three digit
        next_invoice_number = '{0:06d}'.format(last_invoice_number + 1)
        final = str(next_invoice_number)
    # Return custom invoice number
    #return today_string + next_invoice_number
    return  today_string + final

class Ritarget(models.Model):
    ztime = models.DateTimeField(blank=True, null=True)
    zutime = models.DateTimeField(blank=True, null=True)
    zid = models.IntegerField(blank=True, null=True)
    xdate = models.DateField(blank=True, null=True)
    xrow = models.CharField(primary_key=True,max_length=100)
    xziid = models.CharField(max_length=50, blank=True, null=True)
    xtsoid = models.CharField(max_length=50, blank=True, null=True)
    xriid = models.CharField(max_length=50, blank=True, null=True)
    xzone = models.CharField(max_length=100, blank=True, null=True)
    xdiv = models.CharField(max_length=100, blank=True, null=True)
    xqty = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    zemail = models.CharField(max_length=100, blank=True, null=True)
    xemail = models.CharField(max_length=100, blank=True, null=True)
    xyear = models.IntegerField(blank=True, null=True)
    xper = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ritarget'


class Prmst(models.Model):
    xemp = models.CharField(primary_key=True, max_length=100)
    xname = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'prmst'




class Student(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


class Matching(Base):
    __tablename__ = 'Matching'
    matchnum = Column(String, primary_key=True)
    xrow = Column(String(50), primary_key=True)
    xcus = Column(String(50))
    xdornum = Column(String(50))

