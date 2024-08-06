from django.db import models
import re
from datetime import datetime

class UserManager(models.Manager):
    def signup_validator(self, postData):
        errors = {}
        # Add a firstname and validate that firstname at least 2 characters
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters long."

        # Add a lastname and validate that lastname at least 2 characters
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters long."

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address."

        if User.objects.filter(email=postData['email']).exists():
            errors['email'] = "Email address already exists."

        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters long."

        if postData['password']!=postData['confirm_password']:
            errors['confirm_password'] = "Passwords do not match."
        
         # Add a birthday field and validate that the user is at least 18 years old 
        # current_year = datetime.now().year
        # if postData['date_of_birth'].year > current_year - 18:
        #     errors['date_of_birth'] = "You must be at least 18 years old."
        
        # Add a phone number and validate that the user's number should be at least 10 digits
        if len(postData['phone_number']) < 10:
            errors['phone_number'] = "Phone number should be at least 10 digits long."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()  
    

    def __str__(self):
        return self.first_name + self.last_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='img/')
    total=models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User,related_name="products",null=True,blank=True)


    def __str__(self):
        return self.name
    
def create_account(request,pw_hash):
    first_name=request['first_name']
    last_name=request['last_name']
    email=request['email']
    password=pw_hash
    date_of_birth=request['date_of_birth']
    phone_number=request['phone_number']
    return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, date_of_birth=date_of_birth, phone_number=phone_number)

