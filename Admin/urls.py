from django.urls import path,include
from Admin import views
app_name="webadmin"


urlpatterns = [
    path('District/',views.district,name='District'),
    path('Place/',views.place,name='place'),
    path('StationMasterRegistration/',views.stationmasterregistration,name='stationmasterregistration'),
    path('ajax_place/',views.ajax_place,name='AjaxPlace'),
    path('del_district/<int:did>',views.del_district,name='Del_district'),
    path('update_district/<int:did>',views.update_district,name='Update_district'),
    path('EventType/',views.event_type,name="event_type"),
    path('Del_eventtype/<int:did>',views.del_eventtype,name='del_eventtype'),
    path('Update_eventtype/<int:did>',views.update_eventtype,name='update_eventtype'),
     
    path('TicketType/',views.ticket_type,name='tickettype'),
    path('DelTicketType/<int:did>',views.del_tickettype,name='Del_tickettype'),
    path('Update_tickettype/<int:did>',views.update_tickettype,name='update_tickettype'),

    path('Boat/',views.boat,name='boat'),
    path('Del_Boat/<int:did>',views.del_boat,name='del_boat'),
    path('Update_boat/<int:did>',views.update_boat,name='update_boat'),

    path('AddEvent/',views.addevent,name='addevent'),

    path('Food/',views.food,name='food'),
    path('Del_food/<int:did>',views.del_food,name='del_food'),
    path('Update_food/<int:did>',views.update_food,name='update_food'),

    path('Stock/<int:did>',views.stock,name='stock_food'),

    path('ViewComplaint/',views.viewcomplaint,name='viewcomplaint'),
    path('Reply/<int:did>',views.reply,name='reply'),

  
   
    

]                               
