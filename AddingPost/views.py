from AddingPost.models import PostText
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("Username Taken")
            elif User.objects.filter(email=email).exists():
                print("email taken")   
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)  

                user.save()
                print("user create")
                return redirect('login')
        else:
            print("password not match")
        return redirect('/')    
    else:
        return render(request,'register.html')          

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        users=auth.authenticate(username=username,password=password)
        if users is not None:
            auth.login(request,users)
            return redirect("Postcreate")
        else:
            messages.info(request,'invalid creadints')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')     

# Get the text intems by current user according
def Postcreate(request):
    user=request.user
    posts=PostText.objects.filter(user=user)     
    return render(request,"Postcreate.html",{'posts':posts}) 

@login_required
def textPost(request):
    posts=PostText.objects.all()
    if request.method=="POST":
        user=request.user
        text=request.POST['text']
        texts=PostText(user=user,text=text)
        texts.save()
        return redirect('Postcreate')
    else:

        return render(request,"textPost.html")    


        
          


