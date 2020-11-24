from django.db import models


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

class Ritarget(models.Model):
    ztime = models.DateTimeField(blank=True, null=True)
    zutime = models.DateTimeField(blank=True, null=True)
    zid = models.IntegerField(blank=True, null=True)
    xdate = models.DateField(blank=True, null=True)
    xrow = models.IntegerField(primary_key=True)
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







