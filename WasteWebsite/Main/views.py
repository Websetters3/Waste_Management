from django.shortcuts import render
from django.http import HttpResponse
from .models import  Info
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth  import authenticate,  login, logout
from django.views.decorators.csrf import csrf_exempt
#username=Manas
#password=1234
def index(request):
    return HttpResponse("We are at Main")

def wet(request):
    #return HttpResponse("We are at wet waste")
    return render(request, 'wet.html')

def ewaste(request):
    #return HttpResponse("We are at Ewaste")
    return render(request, 'ewaste.html')

def plastic(request):
    #return HttpResponse("We are at plastic")
    return render(request, 'plastic.html')

def other(request):
    #return HttpResponse("We are at other")
    return render(request, 'other.html')

def case(request):
    #return HttpResponse("We are at Case study")
    return render(request, 'case.html') 

def links(request):
    #return HttpResponse("We are at Major Links")
    return render(request, 'links.html') 
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        info=Info(name=name, email=email, phone=phone, desc=desc)
        info.save()
    return render(request, 'contact.html') 

def about(request):
    return render(request, 'about.html') 

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')

        if User.objects.filter(username=username).exists():
            '''if (pass1!= pass2):
                #if User.objects.filter(username=username).exists():
                messages.error(request, " Passwords do not match")
                return redirect('/')'''
        #else:
            messages.error(request, " Username already Exists")

        if (pass1!= pass2):
                #if User.objects.filter(username=username).exists():
                messages.error(request, " Passwords do not match")
                return redirect('/')

        #myuser = User.objects.create_user(username=username, email=email,fname=fname,lname=lname, pass1=pass1,apss2=pass2)
        #myuser.first_name= fname
        #myuser.last_name= lname
        #myuser.save()
        #messages.success(request, " Your iCoder has been successfully created")
        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Account has been successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")
@csrf_exempt
def handleLogin(request):
    #return HttpResponse("login")


    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=auth.authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/')

    return HttpResponse("404- Not found")

def handleLogout(request):
    #return HttpResponse("logout")
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
