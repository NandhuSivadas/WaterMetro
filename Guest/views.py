from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *

# Create your views here.

   
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
        if admincount > 0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('webadmin:Homepage')
        elif stationmastercount > 0:
            stationmasterdata=tbl_stationmaster.objects.get(user_email=email,user_password=password)
            request.session['uid']=stationmasterdata.id
            return redirect('WebStationMaster:Homepage')
        else:
            msg="Invalid credentials!!"
            return render(request,'Guest/Login.html',{'msg':msg})
    else:
        return render(request,'Guest/Login.html')