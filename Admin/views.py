from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *


# Create your views here.

def homepage(request):
    AdminData=tbl_admin.objects.get(id=request.session['aid'])
    usercount=tbl_user.objects.all().count()
    stationcount=tbl_stationmaster.objects.all()
    count=tbl_stationmaster.objects.all().count()
    return render(request,"Admin/Homepage.html",{'Admin':AdminData,'Ucount':usercount,'Scount':stationcount,'count':count}) 

def stationmasterregistration(request):
    disdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        gender=request.POST.get("txt_gender")   
        address=request.POST.get("txt_address")  
        photo=request.FILES.get("txt_file")
        proof=request.FILES.get("txt_proof")
        password=request.POST.get("txt_password")
        tbl_stationmaster.objects.create(master_name=name,master_contact=contact,master_email=email,master_gender=gender,master_address=address,master_photo=photo,master_proof=proof,master_password=password)


        return render(request,'Admin/StationMasterRegistration.html',{'Ddata':disdata,'Pdata':placedata})
    else:

        return render(request,'Admin/StationMasterRegistration.html',{'Ddata':disdata,'Pdata':placedata})


    
def delete_stationmaster(request,did):
    tbl_stationmaster.objects.get(id=did).delete()
    return redirect('webadmin:homepage')






def ajax_place(request):
    disob=tbl_district.objects.get(id=request.GET.get('DIST'))
    places=tbl_place.objects.filter(district=disob)
    print(places)
    return render(request,"Admin/AjaxPlace.html",{'Pdata':places})      


def district(request):
    disob=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get("txt_district")
        tbl_district.objects.create(district_name=district) #to insert data into the tbl
        return render(request,'Admin/District.html',{'Data':disob})
    else:
        return render(request,'Admin/District.html',{'Data':disob})
    

def place(request):
    disdata=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        distid=tbl_district.objects.get(id=request.POST.get("dropdown"))
        placed=request.POST.get("place")
        
        tbl_place.objects.create(place_name=placed,district=distid)
        return render(request,'Admin/Place.html',{'Ddata':disdata,'place':place})
    else:       

        return render(request,'Admin/Place.html',{'Ddata':disdata,'place':place})
    

def del_place(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('webadmin:place')

def update_place(request,did):
    updata=tbl_place.objects.get(id=did)
    disob=tbl_place.objects.all()
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        updata.place_name=request.POST.get("place")
        updata.district=tbl_district.objects.get(id=request.POST.get("dropdown"))
        updata.save()
        return redirect('webadmin:place')
    else:
        return render(request,'Admin/Place.html',{'Ddata':disdata,'udata':updata})

    
def del_district(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('webadmin:District')


def update_district(request,did):
    updata=tbl_district.objects.get(id=did)
    disob=tbl_district.objects.all()
    if request.method=="POST":
        updata.district_name=request.POST.get("txt_district")
        updata.save()
        return render(request,"Admin/District.html",{'Data':disob})
    else:
        return render(request,'Admin/District.html',{'Data':disob,'udata':updata})
    

def event_type(request):
    obj=tbl_eventtype.objects.all()
    if request.method=="POST":
        tbl_eventtype.objects.create(event_type=request.POST.get("txt_eventtype"))
        return render(request,'Admin/EventType.html',{'Data':obj})
    else:
        return render(request,'Admin/EventType.html',{'Data':obj})

def del_eventtype(request,did):
    tbl_eventtype.objects.get(id=did).delete()
    return redirect('webadmin:event_type')


def update_eventtype(request,did):
    updata=tbl_eventtype.objects.get(id=did)
    disob=tbl_eventtype.objects.all()
    if request.method=="POST":
        updata.event_type=request.POST.get("txt_eventtype")
        updata.save()
        return render(request,"Admin/EventType.html",{'Data':disob})
    else:
        return render(request,'Admin/EventType.html',{'Data':disob,'udata':updata})
    
def ticket_type(request):
    TicketTypeData=tbl_tickettype.objects.all()
    if request.method=="POST":
        tbl_tickettype.objects.create(ticket_type=request.POST.get("txt_type")
                                        ,ticket_type_rate=request.POST.get("txt_rate"))
        return render(request,'Admin/TicketType.html',{'Data': TicketTypeData})
    else:
        return render(request,'Admin/TicketType.html',{'Data': TicketTypeData})
        
def del_tickettype(request,did):
    tbl_tickettype.objects.get(id=did).delete()
    return redirect('webadmin:tickettype')


def update_tickettype(request,did):
    updata=tbl_tickettype.objects.get(id=did)
    disob=tbl_tickettype.objects.all()
    if request.method=="POST":
        updata.ticket_type=request.POST.get("txt_type")
        updata.ticket_type_rate=request.POST.get("txt_rate")
        updata.save()
        return render(request,"Admin/TicketType.html",{'Data':disob})
    else:
        return render(request,'Admin/TicketType.html',{'Data':disob,'udata':updata})
    
def boat(request):
    BoatData=tbl_boat.objects.all()
    if request.method=="POST":
        tbl_boat.objects.create(boat_name=request.POST.get("txt_name"),
                                boat_capacity=request.POST.get("txt_capacity")
                                ,boat_entrydate=request.POST.get("txt_entrydate"))
        return render(request,'Admin/Boat.html',{'Data':BoatData})
    else:
        for i in BoatData:
            print(i.boat_entrydate)
        return render(request,'Admin/Boat.html',{'Data':BoatData})

def del_boat(request,did):
    tbl_boat.objects.get(id=did).delete()
    return redirect('webadmin:boat')

def update_boat(request,did):
    updata=tbl_boat.objects.get(id=did)
    if request.method=="POST":
        updata.boat_name=request.POST.get("txt_name")
        updata.boat_capacity=request.POST.get("txt_capacity")
        updata.boat_entrydate=request.POST.get("txt_entrydate")
        updata.save()
        return redirect('webadmin:boat')
    else:
        return render(request,'Admin/Boat.html',{'udata':updata})

def addevent(request):
    EventData=tbl_eventtype.objects.all()
    AddEventData=tbl_addevent.objects.all()
    if request.method=="POST":
        tbl_addevent.objects.create(addevent_title=request.POST.get("txt_title"),
                                    addevent_eventtype=tbl_eventtype.objects.get(id=request.POST.get("select")),     
                                    addevent_details=request.POST.get("txt_details"),
                                    addevent_passengercount=request.POST.get("txt_capacity"),
                                    addevent_rate=request.POST.get("txt_rate"))
        return render(request,'Admin/AddEvent.html',{'Data':EventData,'EventData':AddEventData})
    else:
        return render(request,'Admin/AddEvent.html',{'Data':EventData,'EventData':AddEventData})
    

def del_event(request,did):
    tbl_addevent.objects.get(id=did).delete()
    return redirect('webadmin:addevent')

def update_event(request,did):
    EventData=tbl_eventtype.objects.all()
    updata=tbl_addevent.objects.get(id=did)
    if request.method=='POST':
        updata.addevent_title=request.POST.get("txt_title")
        updata.addevent_eventtype=tbl_eventtype.objects.get(id=request.POST.get("select"))
        updata.addevent_details=request.POST.get("txt_details")
        updata.addevent_passengercount=request.POST.get("txt_capacity")
        updata.save()
        return redirect('webadmin:addevent')
    else:
        return render(request,'Admin/AddEvent.html',{'Data':EventData,'updata':updata})
    
def food(request):
    FoodData=tbl_food.objects.all()
    if request.method=="POST" :
        tbl_food.objects.create(food_name=request.POST.get("txt_name"),
                                food_description=request.POST.get("txt_description"),
                                food_image=request.FILES.get("txt_file"),
                                food_rate=request.POST.get("txt_rate"))
        return render(request,'Admin/Food.html',{'Data':FoodData})
    else:
        return render(request,'Admin/Food.html',{'Data':FoodData})
    

def del_food(request,did):
    tbl_food.objects.get(id=did).delete()
    return redirect('webadmin:food')

def update_food(request,did):
    updata=tbl_food.objects.get(id=did)
    if request.method=="POST":
        updata.food_name=request.POST.get("txt_name")
        updata.food_description=request.POST.get("txt_description")
        updata.food_image=request.POST.get("txt_image")
        updata.food_rate=request.POST.get("txt_rate")
        updata.save()
        return redirect('webadmin:food')
    else:
        return render(request,'Admin/Food.html',{'udata':updata})





def stock(request,did):
    food=tbl_food.objects.get(id=did)
    stockdata=tbl_stock.objects.filter(product=food)
    if request.method=="POST":
        count=tbl_stock.objects.filter(product=food).count()
        if count > 0:
            stockData=tbl_stock.objects.get(product=food)
            stockData.stock_name=int(stockData.stock_name) + int(request.POST.get("txt_stock"))
            stockData.product=food
            stockData.save()
            return redirect("webadmin:stock_food",did=did)
        else:
            tbl_stock.objects.create(stock_name=request.POST.get("txt_stock"),
                                 product=food)
            return render(request,"Admin/Stock.html",{'stock':stockdata})
    else:
        return render(request,"Admin/Stock.html",{'stock':stockdata})



def viewcomplaint(request):
    replydata=tbl_complaint.objects.filter(status=1)
    complaintdata=tbl_complaint.objects.filter(status=0)
    return render(request,'Admin/ViewComplaint.html',{'Data':complaintdata,'ReplyData':replydata})

def reply(request,did):
    data=tbl_complaint.objects.get(id=did)    
    if request.method=="POST":
        reply=request.POST.get('txt_reply')
        data.reply=reply
        data.status=1
        data.save()
        return redirect('webadmin:viewcomplaint')
    else:
        return render(request,'Admin/Reply.html')        

def delete_stock(request,id):
    tbl_stock.objects.get(id=id).delete()
    return redirect("webadmin:food")

def logout(request):
    del request.session["aid"]
    return redirect("wguest:login")


def ajaxreport(request):
    if (request.GET.get("fdate")!="") and (request.GET.get("tdate")!="") and (request.GET.get("status")!=""):
        booking = tbl_ticketbooking.objects.filter(date__gte=request.GET.get("fdate"),date__lte=request.GET.get("tdate"),status=request.GET.get("status"))
        return render(request,"Admin/AjaxReport.html",{"booking":booking})
    elif (request.GET.get("fdate")!="") and (request.GET.get("status")!=""):
        booking = tbl_ticketbooking.objects.filter(date__gte=request.GET.get("fdate"),status=request.GET.get("status"))
        return render(request,"Admin/AjaxReport.html",{"booking":booking})
    elif (request.GET.get("tdate")!="") and (request.GET.get("status")!=""):
        booking = tbl_ticketbooking.objects.filter(date__lte=request.GET.get("tdate"),status=request.GET.get("status"))
        return render(request,"Admin/AjaxReport.html",{"booking":booking})
    elif request.GET.get("fdate")!="":
        booking = tbl_ticketbooking.objects.filter(date__gte=request.GET.get("fdate"))
        return render(request,"Admin/AjaxReport.html",{"booking":booking})
    elif request.GET.get("tdate")!="":
        booking = tbl_ticketbooking.objects.filter(date__lte=request.GET.get("tdate"))
        return render(request,"Admin/AjaxReport.html",{"booking":booking})
    elif request.GET.get("status")!="":
        booking = tbl_ticketbooking.objects.filter(status=request.GET.get("status"))
        return render(request,"Admin/AjaxReport.html",{"booking":booking})
    
def report(request):
    booking = tbl_ticketbooking.objects.all()
    return render(request,'Admin/Report.html',{"booking":booking})
