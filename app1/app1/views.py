from asyncio.windows_events import NULL
from multiprocessing import context
from pickle import NONE
from tarfile import NUL
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import  bcrypt
from django.http import JsonResponse ,HttpResponse
import json


# Create your views here.
def home(request):
    return redirect('/home')
def home1(request):
    if 'id' in request.session:
        user1=Users.objects.get(id=request.session["id"])
    else:
        user1=None
    
    
    context={'user':user1}
    return render(request,'home.html',context)


def reg(request):
    return render(request,'reg.html')
def pc(request):
    if 'id' in request.session:
        user1=Users.objects.get(id=request.session["id"])
    else:
        user1=None
    if 'modellow' in request.session:
        modellow1=request.session['modellow']
    else:
        modellow1=NULL
    if 'pricelow' in request.session:
        pricelow1=request.session['pricelow']
    else:
        pricelow1=NULL
    if 'modelmax' in request.session:
        modelmax1=request.session['modelmax']
    else:
        modelmax1=NULL
    if 'pricemax' in request.session:
        pricemax1=request.session['pricemax']
    else:
        pricemax1=NULL

    context={'user':user1,
    
            
            'all_product':products.objects.all(),
            'filter':products.objects.filter(model_y__lte=modelmax1,model_y__gte=modellow1,price__lte=pricemax1,price__gte=pricelow1)
            
            
            }
    return render(request,'pc.html',context)
    
    
def loginPro(request):
    user = Users.objects.filter(email=request.POST['email']) 
    if user: 
        logged_user = user[0] 
    
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session["id"]=logged_user.id
    
            return redirect('/home')
        else:
            messages.error(request, 'invalid email or password')
            return redirect("/login")
    else:
        messages.error(request, 'invalid email or password')
        return redirect("/login")
def phones(request):
    if 'id' in request.session:
        user1=Users.objects.get(id=request.session["id"])
    else:
        user1=None
    if 'modellow' in request.session:
        modellow1=request.session['modellow']
    else:
        modellow1=NULL
    if 'pricelow' in request.session:
        pricelow1=request.session['pricelow']
    else:
        pricelow1=NULL
    if 'modelmax' in request.session:
        modelmax1=request.session['modelmax']
    else:
        modelmax1=NULL
    if 'pricemax' in request.session:
        pricemax1=request.session['pricemax']
    else:
        pricemax1=NULL

    context={'user':user1,
    
            
            'all_product':products.objects.all(),
            'filter':products.objects.filter(model_y__lte=modelmax1,model_y__gte=modellow1,price__lte=pricemax1,price__gte=pricelow1)
            
            
            }
    return render(request,'phones.html',context)
    
    
def electronicTool(request):
    
    if 'id' in request.session:
        user1=Users.objects.get(id=request.session["id"])
    else:
        user1=None
    if 'modellow' in request.session:
        modellow1=request.session['modellow']
    else:
        modellow1=NULL
    if 'pricelow' in request.session:
        pricelow1=request.session['pricelow']
    else:
        pricelow1=NULL
    if 'modelmax' in request.session:
        modelmax1=request.session['modelmax']
    else:
        modelmax1=NULL
    if 'pricemax' in request.session:
        pricemax1=request.session['pricemax']
    else:
        pricemax1=NULL

    context={'user':user1,
    
            
            'all_product':products.objects.all(),
            'filter':products.objects.filter(model_y__lte=modelmax1,model_y__gte=modellow1,price__lte=pricemax1,price__gte=pricelow1)
            
            
            }
    return render(request,'electronicTool.html ',context)
    
    
def pro123(request):
    context={'all_orders':orders.objects.all(),
    'all_products':products.objects.all()
    }
    return render(request,'admin.html',context)
def show(request,id):
    if 'id' in request.session:
        user1=Users.objects.get(id=request.session["id"])
    else:
        user1=None
    context={'product':products.objects.get(id=id),
    'user':user1
    }
    return render(request,'showproduct.html',context)
def regProc(request):
    errors1 = Users.objects.basic_validator(request.POST)
    errors2 = location.objects.basic_validator(request.POST)
    if len(errors1) > 0 or len(errors2) >0:
        for key, value in errors1.items():
            messages.error(request, value)
        for key, value in errors2.items():
            messages.error(request, value)
        
        return redirect('/reg')
    else:


        hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        location.objects.create(city=request.POST['city'],region=request.POST['region'],street=request.POST['street'],building=request.POST['building'],apartment=request.POST['apartment'])
        x=location.objects.last()
        y=Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=hash,phone_number=request.POST['phone_number'],location=x)
        request.session["id"]=y.id
        return redirect('/home')
def addproduct(request):
    errors = products.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/pro123')
    else:
        products.objects.create(name=request.POST['name'],
        model_y=request.POST['model'],
        description=request.POST['desc'],
        price=request.POST['price'],
        categotry=categories.objects.get(category=request.POST['catagory']),
        image=request.FILES['image'],
        quantity=request.POST['quantity']
        )
        return redirect('/pro123')
def logout(request):
    request.session.clear()
    return redirect('/home')
def login(request):
    return render(request,'login.html')
def add_order(request):
    if 'id' in request.session:


        product=products.objects.get(id=request.POST['id'])
        user=Users.objects.get(id=request.session['id'])

        orders.objects.create(user=user,product=product)
        print("x"*10)
    
    

        return JsonResponse({"class":True})
def isDeliver(request):
    x=orders.objects.get(id=request.POST['id'])
    x.state=True
    x.save()
    
    return redirect('/pro123')



def filter(request):
    model=request.POST['model']
    modellow=model[5]+model[6]+model[7]+model[8]
    modelmax=model[0]+model[1]+model[2]+model[3]
    price=request.POST['price']
    pricelow=price[6]+price[7]+price[8]+price[9]+price[10]
    pricemax=price[0]+price[1]+price[2]+price[3]+price[4]


    request.session['modellow']=int(modellow)
    request.session['modelmax']=int(modelmax)
    request.session['pricelow']=int(pricelow)
    request.session['pricemax']=int(pricemax)

    return redirect('/'+request.POST['submit'])
def about_us(request):
    if 'id' in request.session:
        user1=Users.objects.get(id=request.session["id"])
    else:
        user1=None
    
    return render (request,'about_us.html',{'user':user1})
def deleteOrder(request):
    x=orders.objects.get(id=request.POST['id'])
    y=x.product
    y.quantity-=1
    y.save()
    

    
    
    x.delete()
    
    
    return redirect('/pro123')


