from django.contrib import messages
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def home (request):
    return render(request,'home.html')

def about_us (request):
    return render (request,'about_us.html')

def contact_us (request):
    return render (request,'contact_us.html')


def service (request):
    return render (request,'service.html')

def email(request):
    if request.method=='POST':
        name=request.POST['name'].strip()   
        email=request.POST['email'].strip()    
        mobile=request.POST['mobile'].strip()    
        enquiry=request.POST['enquiry'].strip()
        if name and email and mobile and enquiry:
            subject="Enquiry from Website"
            matter=f"{name} and {email} and {mobile} and {enquiry}"
            from_email='rohit9258736537@gmail.com'
            try:
                send_mail('subject','matter', 'rohit9258736537@gmail.com',"info@sunrealfacility.com")

            except:
                messages.info(request,"Email not Sent , Please try Again")
                return render(request,'contact_us.html')
                
        else:
            messages.info(request,"All Fields Mandatory, Please try Again, Thank You")    
            return render(request,'contact_us.html')

    else:
        messages.info(request,"All Fields Mandatory, Please try Again, Thank You")
        return render(request,'contact_us.html')