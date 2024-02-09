from django.shortcuts import render,redirect
from Admin.models import *
from StationMaster.models import *

# Create your views here.

def home_page(request):
    stationmaster=tbl_stationmaster.objects.get(id=request.session['uid'])
    return render(request,'User/Homepage.html',{' stationmaster': stationmaster})


def service(request):
    sdata=tbl_service.objects.all()
    if request.method=="POST":
        tbl_service.objects.create(start_point=request.POST.get("txt_startpoint"),end_point=request.POST.get("txt_endpoint"))
        return render(request,'StationMaster/Services.html',{'Data':sdata})
    else:
        return render(request,'StationMaster/Services.html',{'Data':sdata})
    

def my_profile(request):
    if request.method=="POST":
        stationmaster=tbl_stationmaster.objects.get(id=request.session['uid'])
        return render(request,'StationMaster/MyProfile.html',{' stationmaster': stationmaster})
    else:
        return render(request,'StationMaster/MyProfile.html')

def edit_profile(request):
    if request.method=="POST":
        stationmaster=tbl_stationmaster.objects.get(id=request.session['uid'])
        stationmaster.master_name=request.POST.get("txt_name")
        stationmaster.master_contact=request.POST.get("txt_contact")
        stationmaster.master_email=request.POST.get("txt_email")
        stationmaster.master_address=request.POST.get("txt_address")
        stationmaster.save()
        return render(request,'StationMaster/EditProfile.html',{' stationmaster': stationmaster})
    
    else:
        return render(request,'StationMaster/EditProfile.html',{' stationmaster': stationmaster})
    
def changepassword(request):
    stationmaster=stationmaster.objects.get(id=request.session['uid'])
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




