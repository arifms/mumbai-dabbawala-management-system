from django.shortcuts import render,redirect
from django.contrib import messages
from .form import *
from django.contrib.auth import login,logout,authenticate
from .models import  canteenItems,customer
# Create your views here.
def index(request):
    
    return render(request,'index.html')
def loginPage(request):
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)         
        if user is not None:
            login(request,user)
            messages.success(request,f"successfully logged in as {username}")
            return redirect('index')
                
           
        else:
            messages.info(request,"login failed")
            return render(request,'login.html')
        
    else:
        return render(request,'login.html')
def logoutPage(request):
    logout(request)
    return redirect('login')
def canteen(request):
    items=canteenItems.objects.all()
    return render(request,'canteen.html',{'items':items})
def adddabba(request):
    return render(request,'adddabba.html')
def register(request):
    form=registerForm()
    if request.method=="POST":
        form=registerForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password1')==form.cleaned_data.get('password2'):
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,"account created successfully for "+user)
                return redirect("login")
            else:
                messages.info(request,'password not matched')
        else:
            messages.error(request,"error")
            return render(request,'register.html',{'form':form})
    else:
        return render(request,'register.html',{'form':form})
def forgot(request):
    return render(request,'forget.html')
def dabbawala(request):
    return render(request,'dabbawala.html')
#Cart items
def cart(request):
    items=canteenItems.objects.all()
    return render(request,'cart.html',{'items':items})
#payments 
def payments(request):
    if request.method=="POST":
        address=request.POST['address']
        phone=int(request.POST['phone'])
        pincode=int(request.POST['pincode'])
        u=request.user
        c=customer(u,address,phone,pincode)
        c.save()

    return render(request,'payments.html')