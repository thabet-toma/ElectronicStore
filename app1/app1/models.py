from email.policy import default
from django.db import models
import re

class locationManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['region']) < 3:
            errors["region"] = "region  should be at least 2 characters"
        if len(postData['building']) < 3:
            errors["building"] = "building should be at least 2 characters"
        if len(postData['street']) < 3:
            errors["street"] = "street should be at least 2 characters"
        if len(postData['apartment']) < 0:
            errors["apartment"] = "apartment required"
    

        

        return errors


class location(models.Model):

        city=models.CharField(max_length=255)
        region=models.CharField(max_length=255)
        street=models.CharField(max_length=255)
        building=models.CharField(max_length=255)
        apartment=models.CharField(max_length=255)
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)
        objects=locationManager()

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['first_name']) <3:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['phone_number']) < 10:
            errors["phone_number"] = "invalid number"
        if len(postData['email']) < 0:
            errors["email"] = "email is required"
        email_regex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        for i in Users.objects.all():
            if i.email==postData['email']:
                errors['email'] = "this email is already exist in our database"

        if len(postData['password']) < 9:
            errors["password"] = "password should be at least 8 characters"
    
    
        return errors

class Users(models.Model):

    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=14,blank=True,null=True)
    location=models.ForeignKey(location,related_name="user_loc",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
class categories(models.Model):

    category=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
class addproduct(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData['name']) < 4:
            errors["name"] = " name should be at least 3 characters"

        if len(postData['model']) < 1:
            errors["model"] = " modele is required"
    

        if len(postData['desc']) < 3:
            errors["desc"] = "description must be more than 3 characters"

    
    

        return errors
class products(models.Model):

    name=models.CharField(max_length=255)
    model_y=models.IntegerField()
    description=models.TextField()
    price=models.IntegerField()
    categotry=models.ForeignKey(categories,related_name='product',on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images',blank=True,null=True)
    quantity=models.IntegerField(blank=True,null=True)
    objects=addproduct()
class orders(models.Model):


    user=models.ForeignKey(Users,related_name="user_ord",on_delete=models.CASCADE)
    product=models.ForeignKey(products,related_name="order_product",on_delete=models.CASCADE,blank=True,null=True)
    state=models.BooleanField(null=True,default=0)
    product=models.ForeignKey(products,related_name="order_product",on_delete=models.CASCADE,blank=True,null=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)




# Create your models here.
