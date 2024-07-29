from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from datetime import date


# Create your views here.

def index(request):
    error = ""
    if request.method == 'POST':
        sd = request.POST['searchdata']
        connection = Connection.objects.filter(connectionid=sd).first()
        viewbill = Bill.objects.filter(connection=connection,status='Not Paid')
        return render(request, 'viewmybill.html', locals())
    return render(request,'index.html', locals())

def about(request):
    return  render(request, 'about.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'admin_login.html', locals())

def admin_home(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    cus = Customer.objects.all().count()
    conn = Connection.objects.all().count()
    b = Bill.objects.all().count()

    d = {'cus': cus, 'conn': conn, 'b': b}
    return render(request,'admin_home.html', d)

def add_Customer(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        c = request.POST['contact']
        e = request.POST['email']
        a = request.POST['address']
        city = request.POST['city']
        s = request.POST['state']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=e)
            Customer.objects.create(user=user, contact=c, address=a, city=city, state=s)
            error = "no"
        except:
            error = "yes"
    return render(request,'add_Customer.html', locals())

def view_Customer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    customer = Customer.objects.all()
    return render(request,'view_Customer.html', locals())

def edit_Customer(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.get(id=request.user.id)
    customer = Customer.objects.get(id=pid)
    error = False
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        c = request.POST['contact']
        a = request.POST['address']
        city = request.POST['city']
        s = request.POST['state']

        user.first_name = fn
        user.last_name = ln
        customer.contact = c
        customer.address = a
        customer.city = city
        customer.state = s
        user.save()
        customer.save()
        error = True

    d = {'customer': customer, 'user': user, 'error': error}
    return  render(request, 'edit_Customer.html', locals())

def delete_Customer(request,pid):
    customer = Customer.objects.get(id=pid)
    customer.delete()
    return redirect('view_Customer')

def add_Connection(request):
    if not request.user.is_authenticated:
        return redirect(admin_login)
    error = ""
    customer1 = Customer.objects.all()
    if request.method == "POST":
        cid = request.POST['connectionid']
        customerid = request.POST['customerid']
        ctype = request.POST['connectiontype']
        cdate = request.POST['connectionstartdate']
        o = request.POST['occupation']
        cload = request.POST['connectionload']
        pno = request.POST['plotno']
        c = request.POST['city']
        p = request.POST['pincode']
        a = request.POST['address']
        s = request.POST['state']
        d = request.POST['description']

        customer = Customer.objects.get(id=customerid)
        try:
            Connection.objects.create(customer=customer, connectionid=cid, connectiontype=ctype, connectionstartdate=cdate, occupation=o,
                                      connectionload=cload, plotno=pno, city=c, pincode=p, address=a, state=s, description=d)
            error = "no"
        except:
            error = "yes"
    return render(request,'add_Connection.html', locals())

def view_Connection(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    connection = Connection.objects.all()
    return render(request,'view_Connection.html', locals())

def edit_Connection(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    customer = Customer.objects.all()
    connection = Connection.objects.get(id=pid)
    error = False
    if request.method == 'POST':
        cid = request.POST['connectionid']
        customerid = request.POST['customerid']
        ctype = request.POST['connectiontype']
        cdate = request.POST['connectionstartdate']
        o = request.POST['occupation']
        cload = request.POST['connectionload']
        pno = request.POST['plotno']
        c = request.POST['city']
        p = request.POST['pincode']
        a = request.POST['address']
        s = request.POST['state']
        d = request.POST['description']

        customer1 = Customer.objects.get(id=customerid)

        connection.customer = customer1
        connection.connectiontype = ctype
        connection.occupation = o
        connection.connectionload = cload
        connection.plotno = pno
        connection.city = c
        connection.pincode = p
        connection.address = a
        connection.state = s
        connection.description = d
        if cdate:
            connection.connectionstartdate = cdate
        connection.save()
        error = True

    d = {'connection': connection, 'customer': customer, 'error': error}
    return  render(request, 'edit_Connection.html', locals())

def delete_Connection(request,pid):
    connection = Connection.objects.get(id=pid)
    connection.delete()
    return redirect('view_Connection')

def add_Bill(request):
    if not request.user.is_authenticated:
        return redirect(admin_login)
    error = ""
    connection1 = Connection.objects.all()
    if request.method == "POST":
        connectionid = request.POST['connectionid']
        b = request.POST['billformonth']
        creading = request.POST['currentreading']
        preading = request.POST['previousreading']
        t = request.POST['totalunit']
        cpu = request.POST['chargeperunit']
        fa = request.POST['finalamount']
        dd = request.POST['duedate']

        connection = Connection.objects.get(id=connectionid)
        try:
            Bill.objects.create(connection=connection, billformonth=b, currentreading=creading, previousreading=preading,
                                      totalunit=t, chargeperunit=cpu, finalamount=fa, duedate=dd, status='Not Paid')
            error = "no"
        except:
            error = "yes"
    return render(request,'add_Bill.html', locals())

def view_Bill(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    bill = Bill.objects.all()
    return render(request,'view_Bill.html', locals())

def delete_Bill(request,pid):
    bill = Bill.objects.get(id=pid)
    bill.delete()
    return redirect('view_Bill')

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request,'change_password.html', locals())

def Logout(request):
    logout(request)
    return redirect('index')

def payment(request,pid):
    error = ""
    bill = Bill.objects.get(id=pid)
    if request.method == "POST":
        bill.status = "paid"
        try:
            bill.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'payment.html', locals())

def viewmybill(request):
    return render(request,'viewmybill.html', locals())





