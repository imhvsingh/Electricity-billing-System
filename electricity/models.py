from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100, null=True)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Connection(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    connectionid = models.CharField(max_length=10, null=True)
    connectiontype = models.CharField(max_length=100, null=True)
    connectionstartdate = models.DateField(null=True)
    occupation = models.CharField(max_length=100, null=True)
    connectionload = models.CharField(max_length=100, null=True)
    plotno = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.connectionid

class Bill(models.Model):
    connection = models.ForeignKey(Connection,on_delete=models.CASCADE)
    billformonth = models.CharField(max_length=50, null=True)
    currentreading = models.CharField(max_length=50, null=True)
    previousreading = models.CharField(max_length=50, null=True)
    totalunit = models.CharField(max_length=100, null=True)
    chargeperunit = models.CharField(max_length=100, null=True)
    finalamount = models.CharField(max_length=100, null=True)
    duedate = models.DateField(null=True)
    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.billformonth
