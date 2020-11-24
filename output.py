# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
