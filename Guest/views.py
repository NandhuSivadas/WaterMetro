from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
import random
from Admin.models import *
from Guest.models import *

# Create your views here.


def home_page(request):
    return render(request,'Guest/Homepage.html')
   
def userregistration(request):
    disdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST" and request.FILES:
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        gender=request.POST.get("txt_gender")
        address=request.POST.get("txt_address")  
        photo=request.FILES.get("txt_photo")
        proof=request.FILES.get("txt_proof")
        password=request.POST.get("txt_password")
        placeid=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_user.objects.create(user_name=name,user_contact=contact,user_email=email,user_gender=gender,user_address=address,user_photo=photo,user_proof=proof,user_password=password,place=placeid)


        return render(request,'Guest/UserRegistration.html',{'Ddata':disdata,'Pdata':placedata})
    else:

        return render(request,'Guest/UserRegistration.html',{'Ddata':disdata,'Pdata':placedata})



def ajax_place(request):
    disob=tbl_district.objects.get(id=request.GET.get('DIST'))
    places=tbl_place.objects.filter(district=disob)
    return render(request,"Guest/AjaxPlace.html",{'Pdata':places})

def login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_pass")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        stationmastercount=tbl_stationmaster.objects.filter(master_email=email,master_password=password).count()
        if usercount > 0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect('webuser:homepage')
        elif admincount > 0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('webadmin:homepage')
        elif stationmastercount > 0:
            stationmasterdata=tbl_stationmaster.objects.get(master_email=email,master_password=password)
            request.session['sid']=stationmasterdata.id
            return redirect('WebStationMaster:homepage')
        else:
            msg="Invalid credentials!!"
            return render(request,'Guest/Login.html',{'msg':msg})
    else:
        return render(request,'Guest/Login.html')

def ForgetPassword(request):
    
    if request.method=="POST":
        otp=random.randint(10000, 999999)
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txtemail')
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour OTP for Reset Password Is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return redirect("wguest:verification")
    else:
        return render(request,"Guest/ForgetPassword.html")
        

def OtpVerification(request):
    if request.method=="POST":
        otp=int(request.session["otp"])
        if int(request.POST.get('txtotp'))==otp:
            userdata=tbl_user.objects.get(user_email=email)
            request.session['uid']=userdata.id
            return redirect('webuser:homepage')
    return render(request,"Guest/Gverify.html")

def CreateNewPass(request):
    if request.method=="POST":
        if request.POST.get('txtpassword2')==request.POST.get('txtpassword3'):
            usercount=tbl_user.objects.filter(user_email=request.session["femail"]).count()
            if usercount>0:
                user=tbl_user.objects.get(user_email=request.session["femail"])
                user.user_password=request.POST.get('txtpassword2')
                user.save()
                return redirect("wguest:login")
    else:       
        return render(request,"Guest/CreateNewPassword.html")


def ajaxemail(request):
    usercount=tbl_user.objects.filter(user_email=request.GET.get("email")).count() 
    if usercount>0:
        return render(request,"Guest/Ajaxemail.html",{'mess':1})
    else:
         return render(request,"Guest/Ajaxemail.html")

def google(request):
    if request.method=="POST":
        otp=random.randint(10000, 999999)
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txtemail')
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour OTP for Reset Password Is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return redirect("wguest:Gverify")
    else:
        return render(request,"Guest/Glog.html")
    


def Gverify(request):
    if request.method=="POST":
        otp=int(request.session["otp"])
        email=request.session["femail"]
        if int(request.POST.get('txtotp'))==otp:
            userdata=tbl_user.objects.get(user_email=email)
            request.session['uid']=userdata.id
            return redirect('webuser:homepage')
    return render(request,"Guest/OTPVerification.html")
    

def emailvalid(request):
    
    if request.method=="POST":
        otp=random.randint(10000, 999999)
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txt_email')
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour OTP for Reset Password Is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txt_email')],
        )
        return redirect("webguest:user_registration")
    else:
        return render(request,"Guest/UserRegistration.html")

def emailverification(request):
    if request.method=="POST":
        otp=int(request.session["otp"])
        if int(request.POST.get('txtotp'))==otp:
            return redirect("webguest:user_registration")
    return render(request,"Guest/UserRegistration.html")






