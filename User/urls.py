from django.urls import path,include
from User import views
app_name="webuser"

urlpatterns = [
 path('Homepage/',views.home_page,name='homepage'),
 path('MyProfile/',views.my_profile,name='myprofile'),
 path('EditProfile/',views.edit_profile,name='editprofile'),
 path('ChangePassword/',views.change_password,name='changepassword'),
 path('TicketBooking/',views.ticketbooking,name='ticketbooking'),
 path('ajaxrate/',views.ajaxrate,name="ajaxrate"),
 path('Complaint/',views.complaint,name='complaint'),

 path('ViewMyTicket/',views.viewmyticket,name='viewmyticket'),


         
]