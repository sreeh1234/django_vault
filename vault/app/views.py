from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def user_login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        user=authenticate(username=uname,password=password)
        if user:
            login(req,user)
            return redirect(vault)
        else:
            messages.warning(req,'invalid username or password')
            return redirect(user_login)
    return render(req,'login.html')

def user_logout(req):
    logout(req)
    req.session.flush()        
    return redirect(user_login)


def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']        
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
            return redirect(user_login)
        except:
            messages.warning(req,'Email Already Exist')
            return redirect(register)
    else:
        return render(req,'register.html')
    
    
def vault(req):
    file=File.objects.filter(user=req.user)
    return render(req,'vault.html',{'files':file})


def add(req):
        if req.method=='POST':
            user=User.objects.get(pk=id)
            name=req.POST['name']
            file=req.FILES['img']
            data=product.objects.create(user=user,name=name,file=file)
            data.save()
            return redirect(vault)
        return render(req,'add.html')    
