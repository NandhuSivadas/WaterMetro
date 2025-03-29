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
 path('Viewfood/',views.Viewfood,name='Viewfood'),
 path('Addcart/<int:pid>',views.Addcart,name='Addcart'),
 path('Mycart/',views.Mycart,name='Mycart'),
 path('cartqty/',views.CartQty,name='cartqty'),
 path('DelCart/<int:did>',views.DelCart,name='delcart'),
 path('Payment/',views.Payment,name='pay'),
 path('paymentticket/<int:id>',views.paymentticket,name='paymentticket'),
path('Billing/',views.Billing,name='Billing'),
path('cancelbooking/<int:id>',views.cancelbooking,name="cancelbooking"),
path('LogOut/',views.logout,name="logout"),
path('loader/',views.loader,name="loader"),
path('paymentsuc/',views.paymentsuc,name="paymentsuc"),

path('EventList/',views.eventlist,name='eventlist'),
path('EventBooking/<int:did>',views.eventbooking,name='eventbooking'),
path('ViewEventBooking/',views.vieweventbooking,name='vieweventbooking'),

path('paymentevent/<int:id>',views.paymentevent,name='paymentevent'),
path('canceleventbooking/<int:id>',views.canceleventbooking,name='canceleventbooking'),

path('Review/',views.review,name='review'),
path('ReviewLoader/',views.reviewloader,name='reviewloader'),

path('schedule/', views.schedule, name='schedule'),














         
]