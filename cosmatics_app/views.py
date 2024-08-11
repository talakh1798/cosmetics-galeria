from django.shortcuts import render,redirect
from .models import User ,Product
from . import models
from django.contrib import messages
import bcrypt
from django.http import JsonResponse


# this function render the welcome page
def welcome(request):
    return render(request, 'Welcome.html')


# this function attempts to authenticate the user by checking the provided email and password against the database. 
# If authentication is successful, it stores the user's ID and name in the session and redirects to the home page 
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
    


# this function renders the sign up page with a form for the user to input their information
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


# this function logs the user out by clearing their session and redirecting them to the homepage
def logout(request):
    request.session.clear()
    # request.session.flush()
    return redirect('/')


# this function renders the home page with the user's name and a list of products   
def home(request):
    user = User.objects.get(id=request.session['id'])
    request.session['id'] = user.id
    request.session['first_name'] = user.first_name
    request.session['last_name'] = user.last_name
    print(request.session['first_name'])
    return render(request, 'home.html', {'first_name': user.first_name})


# this function renders the makeup page with a list of products and a form for the user to select products and quantities
def makeup(request):
    products = models.get_makeup()
    if request.method == 'POST':
         # Get the selected products and quantities from the form
        selected_products = request.POST.getlist('selected_products')
        # Convert selected products to a list of integers
        quantities = {}
        for product_id in selected_products:
            quantities[product_id] = int(request.POST.get(f'quantity_{product_id}'))
        
        total = 0
        products_data = []
        for product_id, quantity in quantities.items():
            product = Product.objects.get(id=product_id)
            total += float(product.price) * quantity
            products_data.append({
                'name': product.name,
                # Convert price to string
                'price': str(product.price), 
                'quantity': quantity
            })
        
        request.session['total'] = total
        request.session['products_data'] = products_data
        return redirect('purchase')
    return render(request, 'makeup.html', {'products': products})


# this function renders the purchase page with the total cost and a list of selected products
def purchase(request):
    total = request.session.get('total', None)
    products_data = request.session.get('products_data', [])
    return render(request, 'purchase.html', {'total': total, 'products_data': products_data})

# this function renders the skincare page with a list of products and a form for the user to select products and quantities
def skincare(request):
    products = models.get_skincare()
    if request.method == 'POST':
        selected_products = request.POST.getlist('selected_products')
        quantities = {}
        for product_id in selected_products:
            quantities[product_id] = int(request.POST.get(f'quantity_{product_id}'))
        
        total = 0
        products_data = []
        for product_id, quantity in quantities.items():
            product = Product.objects.get(id=product_id)
            total += float(product.price) * quantity
            products_data.append({
                'name': product.name,
                # Convert price to string
                'price': str(product.price), 
                'quantity': quantity
            })
        
        request.session['total'] = total
        request.session['products_data'] = products_data
        return redirect('purchase')
    return render(request, 'skincare.html', {'products': products})


# this function renders the about us page 
def about_us(request):
    return render(request, 'about_us.html')


# Create your views here.
