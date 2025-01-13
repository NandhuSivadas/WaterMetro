from django.urls import path,include
from Admin import views
app_name="webadmin"


urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('District/',views.district,name='District'),

    path('Place/',views.place,name='place'),
    path('Del_Place/<int:did>',views.del_place,name='del_place'),
    path('Update_Place/<int:did>',views.update_place,name='update_place'),





    path('StationMasterRegistration/',views.stationmasterregistration,name='stationmasterregistration'),
    path('delete_stationmaster/<int:did>',views.delete_stationmaster,name='delete_stationmaster'),
    



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
    path('Del_Event/<int:did>',views.del_event,name='del_event'),
    path('Update_Event/<int:did>',views.update_event,name='update_event'),



    path('Food/',views.food,name='food'),
    path('Del_food/<int:did>',views.del_food,name='del_food'),
    path('Update_food/<int:did>',views.update_food,name='update_food'),

    path('Stock/<int:did>',views.stock,name='stock_food'),

    path('ViewComplaint/',views.viewcomplaint,name='viewcomplaint'),
    path('Reply/<int:did>',views.reply,name='reply'),
    path('logout',views.logout,name='logout'),
    path('Report/',views.report,name="report"),
    path('ajaxreport/',views.ajaxreport,name="ajaxreport"),




    path('delete_stock/<int:id>',views.delete_stock,name="delete_stock")
   
    

]                               
