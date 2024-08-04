from django.shortcuts import render,redirect
from .models import User ,Product
from . import models
from django.contrib import messages
import bcrypt


def welcome(request):
    return render(request, 'Welcome.html')

def login(request):
    if request.method == "POST" :
        email=request.POST['email']
        password=request.POST['password']
        user = User.objects.filter(email=email).first()
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if user and bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('home')   
    return render(request, 'login.html', {'error': 'Invalid email or password'})

def sign_up(request):
    if request.method == "POST" : 
        errors = User.objects.signup_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('sign_up')
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()  # create the hash    
            print(pw_hash)
            user=models.create_account(request.POST,pw_hash=pw_hash)
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('login')
    return render(request, 'sign_up.html')

def logout(request):
    request.session.clear()
    # request.session.flush()
    return redirect('/')
   
def home(request):
    return render(request, 'home.html')

def makeup(request):
    products = Product.objects.all()
    if request.method == 'POST':
        price = float(request.POST.get('price',0))
        quantity = int(request.POST.get('quantity',0))
        name = request.POST.get('name','not found')

        total = price * quantity
        request.session['total']= total
        request.session['name']= name
        request.session['price'] = price
        request.session['quantity'] = quantity
        return redirect('purchase')
    return render(request, 'makeup.html', {'products': products})

def purchase(request):
    total = request.session.get('total',None)
    name = request.session.get('name',None)
    price = request.session.get('price',None)
    quantity = request.session.get('quantity',None)
    return render(request, 'purchase.html', {'total': total, 'name': name, 'price': price, 'quantity': quantity})

def skincare(request):
    return render(request, 'skincare.html')

# def submit(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         models.ContactForm.objects.create(name=name, email=email, message=message)
#         return redirect('home')
#     return render(request, 'contact.html')

# Create your views here.
