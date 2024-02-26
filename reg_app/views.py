from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from reg_project import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

# Create your views here.
def sign_up(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('sign_up')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('sign_up')

        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('sign_up')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('sign_up')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('sign_up')
        myuser=User.objects.create_user(username, email, pass1,first_name=fname,last_name=lname)
        myuser.save()
        messages.success(request, "Your Are succesfully registered")
         # Welcome Email
        subject = "Welcome to XYZ!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to XYz!! \nThank you for your registration to our website\n. \n\nThanking You\nAnubhav Madhav"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return render(request,"reg_app/welcome_page.html",{"fname":myuser.first_name})
    return render(request,"reg_app/sign_up.html")

