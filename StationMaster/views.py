from django.shortcuts import render,redirect
from Admin.models import *
from StationMaster.models import *
from User.models import *

# Create your views here.

def home_page(request):
    stationmaster=tbl_stationmaster.objects.get(id=request.session['sid'])
    return render(request,'StationMaster/Homepage.html',{' stationmaster': stationmaster})


def service(request):
    sdata=tbl_service.objects.all()
    if request.method=="POST":
        tbl_service.objects.create(start_point=request.POST.get("txt_startpoint"),end_point=request.POST.get("txt_endpoint"))
        return render(request,'StationMaster/Services.html',{'Data':sdata})
    else:
        return render(request,'StationMaster/Services.html',{'Data':sdata})
    

def my_profile(request):
        stationmaster=tbl_stationmaster.objects.get(id=request.session['sid'])
        print(stationmaster)
        return render(request,'StationMaster/MyProfileNew.html',{'stationmaster': stationmaster})
   

def edit_profile(request):

    stationmaster=tbl_stationmaster.objects.get(id=request.session['sid'])
    if request.method=="POST":
   
        stationmaster.master_name=request.POST.get("txt_name")
        stationmaster.master_contact=request.POST.get("txt_contact")
        stationmaster.master_email=request.POST.get("txt_email")
        stationmaster.master_address=request.POST.get("txt_address")
        stationmaster.save()
        return render(request,'StationMaster/EditProfileNew.html',{'stationmaster': stationmaster})
    
    else:
        return render(request,'StationMaster/EditProfileNew.html',{'stationmaster': stationmaster})
    
def changepassword(request):
    stationmaster=tbl_stationmaster.objects.get(id=request.session['sid'])
    if request.method=="POST":
        currentpass=request.POST.get("txt_currentpassword")
        if stationmaster.master_password == currentpass:
            newpass=request.POST.get("txt_newpassword")
            conpass=request.POST.get("txt_confirmpassword")
            if newpass==conpass:
                stationmaster.master_password=newpass
                stationmaster.save()
                msg="successfully"
                return render(request,'StationMaster/ChangePassword.html',{'msg':msg})
            else:
                msg="Cannot Change Password"
                return render(request,'StationMaster/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'StationMaster/ChangePassword.html',{'msg':msg})

    else:
        return render(request,'StationMaster/ChangePassword.html')
    
def assignboat(request):
    BoatData=tbl_boat.objects.all()
    ServiceData=tbl_service.objects.all()
    assignData=tbl_assignboat.objects.all()
    if request.method=="POST":
        tbl_assignboat.objects.create(boat=tbl_boat.objects.get(id=request.POST.get("boat")),
                                      service=tbl_service.objects.get(id=request.POST.get("selectservice")),
                                      starttime=request.POST.get("txt_starttime"),
                                      arrivaltime=request.POST.get("txt_arrivaltime"))
        return render(request,'StationMaster/AssignBoat.html',{'Data':BoatData,'Sdata':ServiceData,'Adata':assignData})
    else:
        return render(request,'StationMaster/AssignBoat.html',{'Data':BoatData,'Sdata':ServiceData,'Adata':assignData})
 
def del_service(request,did):
    tbl_service.objects.get(id=did).delete()
    return redirect('WebStationMaster:service')

def update_service(request, did):
    updata = tbl_service.objects.get(id=did)

    if request.method == "POST":
        updata.start_point = request.POST.get("txt_startpoint")
        updata.end_point = request.POST.get("txt_endpoint")
        updata.save()
        return redirect('WebStationMaster:service')
    else:
        return render(request, 'StationMaster/Services.html', {'udata':updata})
    
def del_assignboat(request,did):
    tbl_assignboat.objects.get(id=did).delete()
    return redirect('WebStationMaster:assignboat')

def update_assignboat(request,did):
    updata=tbl_assignboat.objects.get(id=did)
    BoatData=tbl_boat.objects.all()
    ServiceData=tbl_service.objects.all()
    if request.method=="POST":
        updata.boat=tbl_boat.objects.get(id=request.POST.get("boat"))
        updata.service=tbl_service.objects.get(id=request.POST.get("selectservice"))
        updata.starttime=request.POST.get("txt_starttime")
        updata.arrivaltime=request.POST.get("txt_arrivaltime")
        updata.save()
        return redirect('WebStationMaster:assignboat')
    else:
        return render(request, 'StationMaster/AssignBoat.html', {'udata':updata,'Data':BoatData,'Sdata':ServiceData})
    
def viewticketbooking(request):
    booking = tbl_ticketbooking.objects.all()
    return render(request,"StationMaster/Viewticketbooking.html",{"booking":booking})

def userboat_assign(request,id):
    boat = tbl_assignboat.objects.all()
    if request.method == "POST":
        assi = tbl_ticketbooking.objects.get(id=id)
        boat = tbl_assignboat.objects.get(id=request.POST.get("sel_boat"))
        assi.assign = boat
        assi.status = 2
        assi.save()
        return render(request,"StationMaster/Viewticketbooking.html",{"msg":"Boat Assigned..."})
    else:
        return render(request,"StationMaster/User_Boat_assign.html",{"boat":boat})

def refund(request,id):
    booking=tbl_ticketbooking.objects.get(id=id)
    amount=booking.book_amount
    if request.method=="POST":
        booking.status = 4
        booking.save()
        return redirect("WebStationMaster:viewticketbooking")
    else:
        return render(request,"StationMaster/Payment.html",{'amnt':amount})

def report(request):
    booking = tbl_ticketbooking.objects.all()
    return render(request,'StationMaster/Report.html',{"booking":booking})

def ajaxreport(request):
    if (request.GET.get("fdate")!="") and (request.GET.get("tdate")!="") and (request.GET.get("status")!=""):
        booking = tbl_ticketbooking.objects.filter(date__gte=request.GET.get("fdate"),date__lte=request.GET.get("tdate"),status=request.GET.get("status"))
        return render(request,"StationMaster/AjaxReport.html",{"booking":booking})
    elif (request.GET.get("fdate")!="") and (request.GET.get("status")!=""):
        booking = tbl_ticketbooking.objects.filter(date__gte=request.GET.get("fdate"),status=request.GET.get("status"))
        return render(request,"StationMaster/AjaxReport.html",{"booking":booking})
    elif (request.GET.get("tdate")!="") and (request.GET.get("status")!=""):
        booking = tbl_ticketbooking.objects.filter(date__lte=request.GET.get("tdate"),status=request.GET.get("status"))
        return render(request,"StationMaster/AjaxReport.html",{"booking":booking})
    elif request.GET.get("fdate")!="":
        booking = tbl_ticketbooking.objects.filter(date__gte=request.GET.get("fdate"))
        return render(request,"StationMaster/AjaxReport.html",{"booking":booking})
    elif request.GET.get("tdate")!="":
        booking = tbl_ticketbooking.objects.filter(date__lte=request.GET.get("tdate"))
        return render(request,"StationMaster/AjaxReport.html",{"booking":booking})
    elif request.GET.get("status")!="":
        booking = tbl_ticketbooking.objects.filter(status=request.GET.get("status"))
        return render(request,"StationMaster/AjaxReport.html",{"booking":booking})

def vieweventbooking(request):
    booking = tbl_eventbooking.objects.all()
    return render(request,"StationMaster/ViewEventBooking.html",{"booking":booking})


def logout(request):
    del request.session["sid"]
    return redirect("wguest:login")

def user_eventboat_assign(request,id):
    boat = tbl_assignboat.objects.all()
    if request.method == "POST":
        assi = tbl_eventbooking.objects.get(id=id)
        boat = tbl_assignboat.objects.get(id=request.POST.get("sel_boat"))
        assi.assign = boat
        assi.status = 2
        assi.save()
        return render(request,"StationMaster/ViewEventbooking.html",{"msg":"Boat Assigned..."})
    else:
        return render(request,"StationMaster/User_Boat_assign.html",{"boat":boat})

def printcard(request):
    return render(request,'StationMaster/PrintCard.html')