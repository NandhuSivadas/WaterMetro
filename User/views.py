from datetime import datetime
import random
from django.shortcuts import render,redirect
from django.contrib import messages
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
                                      ticket_type=tbl_tickettype.objects.get(id=request.POST.get("txt_tickettype")),
                                      Passenger_count=request.POST.get("txt_number"),
                                      book_amount=request.POST.get("txt_amount"),
                                      user=user)
        
        return render(request,'User/TicketBooking.html')
    else:
        return render(request,'User/TicketBooking.html',{'Data':TicketData,'user':user})
    
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
    userid=tbl_user.objects.get(id=request.session['uid'])
    ticketdata=tbl_ticketbooking.objects.filter(user=userid)
    return render(request,'User/ViewMyTicket.html',{'ticket':ticketdata})

def Viewfood(request):
    Food=tbl_food.objects.all()
    return render(request,'User/Food.html',{'food':Food})

def Addcart(request,pid):
    if 'uid' in request.session:
        fooddata=tbl_food.objects.get(id=pid)
        custdata=tbl_user.objects.get(id=request.session["uid"])
        tbl_bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
        if tbl_bookingcount>0:
         tbl_bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
         tbl_cartcount=tbl_cart.objects.filter(booking=tbl_bookingdata,food=fooddata).count()
         if tbl_cartcount>0:
          msg="Already added"
          return render(request,"User/Food.html",{'msg':msg})
         else:
            tbl_cart.objects.create(booking=tbl_bookingdata,food=fooddata,cart_qty=1)
            return redirect("webuser:Viewfood")   
        
        else:
           tbl_booking.objects.create(user=custdata)
           tbl_bookingcount=tbl_booking.objects.filter(booking_status=0,user=custdata).count()
           if tbl_bookingcount>0:
            tbl_bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
            tbl_cartcount=tbl_cart.objects.filter(booking=tbl_bookingdata,food=fooddata).count()
            if tbl_cartcount>0:
             msg=" added"
             return render(request,"User/Food.html",{'msg':msg})
            else:
             tbl_cart.objects.create(booking=tbl_bookingdata,food=fooddata,cart_qty=1)
             return redirect("webuser:Viewfood")
    else:
          return redirect("wguest:login")

def Mycart(request):
   if request.method=="POST":
     bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
     bookingdata.booking_amount=request.POST.get("carttotalamt")
     bookingdata.booking_status=1
     bookingdata.save()
     return redirect("webuser:pay")
   else:
    customerdata=tbl_user.objects.get(id=request.session["uid"])
    bcount=tbl_booking.objects.filter(user=customerdata,booking_status=0).count()
   #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
    if bcount>0:
    #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
     book=tbl_booking.objects.get(user=customerdata,booking_status=0)
     bid=book.id
     request.session["bookingid"]=bid
     bkid=tbl_booking.objects.get(id=bid)
     cartdata=tbl_cart.objects.filter(booking=bkid)
     return render(request,"User/MyCart.html",{'data':cartdata})
    else:
      return render(request,"User/MyCart.html")
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("webuser:Mycart")
def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("webuser:Mycart")

def Payment(request):
   booking=tbl_booking.objects.get(id=request.session["bookingid"])
   amount=booking.booking_amount
   if request.method=="POST":
      booking.payment_status=1
      booking.save()
      return redirect("webuser:Billing")
   else:
    return render(request,"User/Payment.html",{'amnt':amount})
   
def paymentticket(request,id):
   booking=tbl_ticketbooking.objects.get(id=id)
   amount=booking.book_amount
   if request.method=="POST":
      booking.status=1
      booking.save()
      return redirect("webuser:loader")
   else:
    return render(request,"User/Payment.html",{'amnt':amount})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def cancelbooking(request,id):
    booking=tbl_ticketbooking.objects.get(id=id)
    booking.status= 3
    booking.save()
    return redirect("webuser:viewmyticket")

def Billing(request):
    if 'uid' in request.session:
        billno=random.randint(10000,99999)
   
        today = datetime.now()
        today=today.strftime("%d-%m-%Y")
   
        farm=tbl_user.objects.get(id=request.session["uid"])
        uobj=tbl_booking.objects.get(id=request.session['bookingid'])
        amnt=uobj.booking_amount
        cart=tbl_cart.objects.filter(booking=uobj)
        return render(request,"User/Bill.html",{'billno':billno,'today':today,'userdata':farm,'data':cart,'amnt':amnt})
    else:
        return redirect("wguest:login")



def logout(request):
    del request.session["uid"]
    return redirect("wguest:login")


def eventlist(request):
    event=tbl_addevent.objects.all()
    return render(request,'User/EventList.html',{'event':event})

def eventbooking(request,did):
    Event=tbl_addevent.objects.get(id=did)
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        tbl_eventbooking.objects.create(date=request.POST.get("txt_date"),
                                      tickettype=request.POST.get("txt_type"),
                                      Passenger_count=request.POST.get("txt_count"),
                                      book_amount=request.POST.get("txt_rate"),
                                      details=request.POST.get("txt_details"),
                                      user=user)
        err=1
        return render(request,'User/ViewEventBooking.html',{'msg':err})
    else:
        return render(request,'User/EventBooking.html',{'user':user,'Event':Event})

def vieweventbooking(request):
    userid=tbl_user.objects.get(id=request.session['uid'])
    ticketdata=tbl_eventbooking.objects.filter(user=userid)
    return render(request,'User/ViewEventBooking.html',{'ticket':ticketdata})


def paymentevent(request,id):
   booking=tbl_eventbooking.objects.get(id=id)
   amount=booking.book_amount
   if request.method=="POST":
      booking.status=1
      booking.save()
      return redirect("webuser:loader")
   else:
    return render(request,"User/Payment.html",{'amnt':amount})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def canceleventbooking(request,id):
    booking=tbl_eventbooking.objects.get(id=id)
    booking.status= 3
    booking.save()
    return redirect("webuser:viewmyticket")


def review(request):
   if request.method=="POST":
      tbl_review.objects.create(review=request.POST.get("txt_review"))
      return redirect("webuser:reviewloader")
   else:
      return render(request,'User/Review.html')
   
def reviewloader(request):
   return render(request,'User/ReviewLoader.html')