from django.shortcuts import render,redirect
from User.models import *
from Admin.models import *
from Guest.models import *


# Create your views here.
def home_page(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/Homepage.html',{'user':user})

def my_profile(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/MyProfile.html',{'user':user})

def edit_profile(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        user.user_name=request.POST.get("txt_name")
        user.user_email=request.POST.get("txt_email")
        user.user_contact=request.POST.get("txt_contact")
        user.user_address=request.POST.get("txt_address")
        user.save()
        return render(request,'User/EditProfile.html',{'user':user})
    else:
        return render(request,'User/EditProfile.html',{'user':user})
       

  

def change_password(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        currentpass=request.POST.get("txt_currentpassword")
        if user.user_password == currentpass:
            newpass=request.POST.get("txt_newpassword")
            conpass=request.POST.get("txt_confirmpassword")
            if newpass==conpass:
                user.user_password=newpass
                user.save()
                msg="successfully"
                return render(request,'User/ChangePassword.html',{'msg':msg})
            else:
                msg="Cannot Change Password"
                return render(request,'User/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'User/ChangePassword.html',{'msg':msg})

    else:
        return render(request,'User/ChangePassword.html')

def ticketbooking(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    TicketData=tbl_tickettype.objects.all()
    if request.method=="POST":
        tbl_ticketbooking.objects.create(date=request.POST.get("txt_date"),
                                      ticket_type=tbl_tickettype.objects.get(id=request.POST.get("select")),
                                      passenger_count=request.POST.get("txt_count"),
                                      book_amount=request.POST.get("txt_amount"),
                                      user=user)
        
        return render(request,'User/TicketBooking.html')
    else:
        return render(request,'User/ticketBooking.html',{'Data':TicketData,'user':user})
    
def ajaxrate(request):
    if request.GET.get("count") != "":
        ticket = tbl_tickettype.objects.get(id=request.GET.get("tt"))
        rate = int(ticket.ticket_type_rate)
        tot = rate * int(request.GET.get("count"))
        return render(request,"User/Ajaxrate.html",{"rate":tot})
    else:
        return render(request,"User/Ajaxrate.html",{"rate":0})
    
def complaint(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        tbl_complaint.objects.create(title=request.POST.get("txt_title"),
                                     description=request.POST.get("txt_description"),
                                     user=user)
        return redirect('webuser:complaint')
    else:
        return render(request,'User/Complaint.html')

def viewmyticket(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/ViewMyTicket.html')
