from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Product, Cart, Order, O_item, Wishlist
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')


def testimonail(request):
    return render(request, 'testimonail.html')


def about(request):
    return render(request, 'about.html')


def product_agri(request):
    data = Product.objects.all()
    return render(request, 'shop.html', {'data': data})


def cart(request):
    return render(request, 'cart.html')


@login_required(login_url='/login/')
def cart(request):
    data = Cart.objects.filter(u_id=request.user)
    g_total = 0
    for d in data:
        g_total += d.sub_total()

    return render(request, 'cart.html', {'data': data, 'g_total': g_total})


@login_required(login_url='/login/')
def add_cart(request, pid):
    p = Product.objects.get(pid=pid)
    if Cart.objects.filter(u_id=request.user, p_id=p).exists():
        print('Product is already exists...')
        return redirect('/cart/')
    else:
        c = Cart(p_id=p, u_id=request.user, quantity=1)
        c.save()
        print('Product is added to the Cart...')
        return redirect('/cart/')


def plus_cart(request, cid):
    c = Cart.objects.get(cid=cid)
    c.quantity += 1
    c.save()
    print('Quantity is Plus by one...')
    return redirect('/cart/')


def minus_cart(request, cid):
    c = Cart.objects.get(cid=cid)
    if c.quantity > 1:
        c.quantity -= 1
        c.save()
        print('Quantity is Minus by one...')
    else:
        c.delete()
        print('Quantity is Minus by one...')

    return redirect('/cart/')


def delete_cart(request, cid):
    c = Cart.objects.get(cid=cid)
    c.delete()
    print('Product is deleted from cart...')
    return redirect('/cart/')


def wishlist(request):
    return render(request, 'wishlist.html')


@login_required(login_url='/login/')
def add_wishlist(request, pid):
    p = Product.objects.get(pid=pid)
    if Wishlist.objects.filter(u_id=request.user, p_id=p).exists():
        print('Product is already exists...')
        return redirect('/wishlist/')
    else:
        w = Wishlist(p_id=p, u_id=request.user, quantity=1)
        w.save()
        print('Product is added to the Wishlist...')
        return redirect('/wishlist/')


@login_required(login_url='/login/')
def wishlist(request):
    data = Wishlist.objects.filter(u_id=request.user)

    return render(request, 'wishlist.html', {'data': data})


def delete_wishlist(request, wid):
    w = Wishlist.objects.get(wid=wid)
    w.delete()
    print('Product is deleted from wishlist...')
    return redirect('/wishlist/')


def registration_agri(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        uemail = request.POST['uemail']
        upass1 = request.POST['upass1']
        upass2 = request.POST['upass2']

        if upass1 == upass2:
            if User.objects.filter(username=uname).exists():
                print('Username is already exists...')
                return redirect('/registration-agri/')
            elif User.objects.filter(email=uemail).exists():
                print('Email is already exists...')
                return redirect('/registration-agri/')
            else:
                u = User.objects.create_user(
                    first_name=fname, last_name=lname, username=uname, email=uemail, password=upass1)
                u.save()
                print('Successfully Registered...')
                return redirect('/login/')

        else:
            print('Passwords Does not matched...')
            return redirect('/registration-agri/')

    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass1 = request.POST['upass1']

        user = auth.authenticate(username=uname, password=upass1)
        if user:
            auth.login(request, user)
            print('Successfully Logged In.....')
            return redirect('/')
        else:
            print('Invalid credentials.....')
            return redirect('/login/')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    print("Successfully Logged out...")
    return redirect('/')


def checkout(request):
    data = Cart.objects.filter(u_id=request.user)
    g_total = 0
    for d in data:
        g_total += d.sub_total()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        payment = request.POST['payment']

        if payment == '1':
            o = Order(name=name, email=email, phone=phone, address=address, city=city,
                      state=state, zip=zip, p_type='Cash On Delivery', u_id=request.user, amount=g_total)
            o.save()

            for d in data:
                p = Product.objects.get(pid=d.p_id.pid)
                O_item(o_id=o, p_id=p, quantity=d.quantity,
                       sub_total=d.sub_total()).save()
                d.delete()
            print("Order is saved...")
            return redirect('/confirmorder/' + str(o.oid))
    return render(request, 'checkout.html')


def confirmorder(request, oid):
    order_data = Order.objects.get(oid=oid)
    order_item_data = O_item.objects.filter(o_id=oid)
    return render(request, 'confirmorder.html', {'order_data': order_data, 'order_item_data': order_item_data})


def myorders(request):
    data = Order.objects.filter(u_id=request.user)
    return render(request, 'myorders.html',{'data':data})

